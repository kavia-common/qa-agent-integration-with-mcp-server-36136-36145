# Q&A Agent API (Ocean Professional)

Modern REST API for question answering with optional MCP integration.

Base URL: /api

Endpoints:
- GET /api/health/ — Health check
- POST /api/qa/ask/ — Ask a question
- POST /api/mcp/invoke/ — Invoke an MCP tool

Environment variables:
- MCP_BRIDGE_URL: Base URL for MCP HTTP bridge (required for MCP use)
- MCP_API_KEY: Optional Bearer token for MCP
- MCP_VERIFY_TLS: 'true' or 'false' (default true)

OpenAPI docs:
- Swagger UI: /docs
- ReDoc: /redoc
- Spec JSON: /swagger.json

Ocean Professional theme hints are included in response metadata for any consumer UI.

Example request:
POST /api/qa/ask/
{
  "question": "What is MCP?",
  "context": "I use model context protocol",
  "use_mcp": true
}
