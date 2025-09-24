import json
import os
import time
from typing import Any, Dict, Optional, Tuple

import logging
import requests


logger = logging.getLogger(__name__)

DEFAULT_TIMEOUT = 30


class MCPClientError(Exception):
    """Raised for MCP client communication issues."""


# PUBLIC_INTERFACE
class MCPClient:
    """Client to communicate with an MCP server via a bridge endpoint.

    The client uses an HTTP-based bridge assumed to be exposed by the MCP server.
    Configuration is provided via environment variables:

    - MCP_BRIDGE_URL: Base URL of the MCP HTTP bridge (e.g., https://mcp.example.com)
    - MCP_API_KEY: Optional API key for authentication (sent as Bearer token)
    - MCP_VERIFY_TLS: 'true' or 'false' to enable/disable TLS verification (default true)

    The bridge API is expected to expose:
    - POST {MCP_BRIDGE_URL}/tools/invoke -> body: {"tool": "...", "arguments": {...}}
      returns: {"ok": true, "result": {...}} or {"ok": false, "error": "..."}

    For environments without an MCP bridge, the client will raise MCPClientError.
    """

    def __init__(self) -> None:
        self.base_url = os.getenv("MCP_BRIDGE_URL", "").rstrip("/")
        self.api_key = os.getenv("MCP_API_KEY")
        verify_env = os.getenv("MCP_VERIFY_TLS", "true").lower().strip()
        self.verify_tls = verify_env not in {"0", "false", "no"}

        if not self.base_url:
            logger.warning("MCP_BRIDGE_URL is not configured; MCP calls will fail.")

        self._session = requests.Session()
        if self.api_key:
            self._session.headers.update({"Authorization": f"Bearer {self.api_key}"})
        self._session.headers.update({"Content-Type": "application/json"})

    def _url(self, path: str) -> str:
        return f"{self.base_url}{path}"

    # PUBLIC_INTERFACE
    def invoke_tool(
        self, tool: str, arguments: Optional[Dict[str, Any]] = None, timeout: Optional[int] = None
    ) -> Tuple[bool, Dict[str, Any]]:
        """Invoke an MCP tool via the bridge.

        Returns a tuple (ok, payload). When ok is False, payload contains error info.

        Raises MCPClientError for connection or protocol issues.
        """
        if not self.base_url:
            raise MCPClientError("MCP_BRIDGE_URL not configured")

        payload = {"tool": tool, "arguments": arguments or {}}
        to = timeout if timeout is not None else DEFAULT_TIMEOUT

        try:
            start = time.time()
            resp = self._session.post(
                self._url("/tools/invoke"),
                data=json.dumps(payload),
                timeout=to,
                verify=self.verify_tls,
            )
            elapsed = time.time() - start
            data = resp.json() if resp.content else {}
            if resp.status_code >= 400:
                logger.error("MCP bridge error %s: %s", resp.status_code, data)
                return False, {
                    "status": resp.status_code,
                    "error": data if data else resp.text,
                    "elapsed": elapsed,
                }
            if not isinstance(data, dict) or "ok" not in data:
                raise MCPClientError("Invalid MCP bridge response format")
            data["elapsed"] = elapsed
            return bool(data["ok"]), data
        except requests.RequestException as exc:
            logger.exception("MCP bridge request failure")
            raise MCPClientError(str(exc)) from exc
