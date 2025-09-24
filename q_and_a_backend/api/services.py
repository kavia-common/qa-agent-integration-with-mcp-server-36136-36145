import logging
from typing import Any, Dict, Optional

from .mcp_client import MCPClient, MCPClientError


logger = logging.getLogger(__name__)


# PUBLIC_INTERFACE
class QAService:
    """High-level Q&A service that can answer via local logic or by delegating to MCP tools.

    The default local logic is intentionally simple as a placeholder. Real implementations
    can integrate with vector search, LLMs, or knowledge bases.
    """

    def __init__(self) -> None:
        self._mcp = MCPClient()

    def _local_answer(self, question: str, context: Optional[str]) -> Dict[str, Any]:
        """Very basic local placeholder answer."""
        base = "This is a placeholder answer."
        if context:
            base += " I considered the provided context."
        explanation = (
            "Local QA engine used. For production, integrate with your LLM or KB here."
        )
        return {
            "answer": f"{base} You asked: '{question}'",
            "source": "local",
            "meta": {
                "engine": "local-baseline",
                "explanation": explanation,
                # Ocean Professional style hints if rendered in UIs
                "theme": {
                    "primary": "#2563EB",
                    "secondary": "#F59E0B",
                    "error": "#EF4444",
                    "background": "#f9fafb",
                    "surface": "#ffffff",
                    "text": "#111827",
                },
            },
        }

    # PUBLIC_INTERFACE
    def answer(
        self, question: str, context: Optional[str] = None, use_mcp: bool = False
    ) -> Dict[str, Any]:
        """Answer a question, routing to MCP if requested and available."""
        if use_mcp:
            try:
                ok, data = self._mcp.invoke_tool(
                    tool="qa.answer",
                    arguments={"question": question, "context": context or ""},
                )
                if ok:
                    result = data.get("result") or {}
                    # Expecting result: {"answer": "...", "meta": {...}}
                    return {
                        "answer": result.get("answer", "No answer returned by MCP."),
                        "source": "mcp",
                        "meta": result.get("meta", {"bridge_elapsed": data.get("elapsed")}),
                    }
                # Fall back to local if MCP responded with error envelope
                logger.warning("MCP returned error: %s", data)
            except MCPClientError as exc:
                logger.warning("MCP unavailable, falling back to local: %s", exc)
        return self._local_answer(question, context)

    # PUBLIC_INTERFACE
    def invoke_mcp_tool(self, tool: str, arguments: Optional[Dict[str, Any]], timeout: Optional[int]) -> Dict[str, Any]:
        """Invoke an arbitrary MCP tool and return a normalized response."""
        try:
            ok, data = self._mcp.invoke_tool(tool=tool, arguments=arguments or {}, timeout=timeout)
            return {
                "ok": ok,
                "data": data,
            }
        except MCPClientError as exc:
            return {
                "ok": False,
                "data": {"error": str(exc)},
            }
