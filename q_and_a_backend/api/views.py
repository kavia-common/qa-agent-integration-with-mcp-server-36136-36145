from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .serializers import QuestionSerializer, AnswerSerializer, MCPInvokeSerializer
from .services import QAService


# PUBLIC_INTERFACE
@swagger_auto_schema(
    method="get",
    operation_id="health_check",
    operation_summary="Health check",
    operation_description="Returns simple health status for the API service.",
    responses={200: openapi.Response("Healthy", schema=openapi.Schema(type=openapi.TYPE_OBJECT))},
    tags=["system"],
)
@api_view(["GET"])
@permission_classes([AllowAny])
def health(request):
    """Simple health endpoint."""
    return Response({"message": "Server is up!", "theme": {"primary": "#2563EB", "secondary": "#F59E0B"}})


# PUBLIC_INTERFACE
@swagger_auto_schema(
    method="post",
    operation_id="qa_ask",
    operation_summary="Ask a question",
    operation_description="""
Submit a natural-language question and receive an answer.

If 'use_mcp' is true, the service will attempt to route the question
to an MCP server tool named 'qa.answer' via the MCP bridge. If the MCP
request fails, it will fall back to a local baseline answer.

Ocean Professional theme is reflected in returned meta.theme for UI hints.
""",
    request_body=QuestionSerializer,
    responses={
        200: AnswerSerializer,
        400: "Validation error",
    },
    tags=["qa"],
)
@api_view(["POST"])
@permission_classes([AllowAny])
def ask_question(request):
    """Answer a question, optionally using MCP tools."""
    serializer = QuestionSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    svc = QAService()
    payload = serializer.validated_data
    result = svc.answer(
        question=payload["question"],
        context=payload.get("context"),
        use_mcp=payload.get("use_mcp", False),
    )
    out = AnswerSerializer(result)
    return Response(out.data, status=status.HTTP_200_OK)


# PUBLIC_INTERFACE
@swagger_auto_schema(
    method="post",
    operation_id="mcp_invoke",
    operation_summary="Invoke an MCP tool",
    operation_description="""
Directly invoke an MCP tool via the configured MCP HTTP bridge.

Requires environment configuration:
- MCP_BRIDGE_URL
- Optional: MCP_API_KEY, MCP_VERIFY_TLS

Returns a normalized response with ok/data fields.
""",
    request_body=MCPInvokeSerializer,
    responses={200: openapi.Response("Invocation result", schema=openapi.Schema(type=openapi.TYPE_OBJECT))},
    tags=["mcp"],
)
@api_view(["POST"])
@permission_classes([AllowAny])
def mcp_invoke(request):
    """Invoke an MCP tool by name."""
    serializer = MCPInvokeSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    svc = QAService()
    data = svc.invoke_mcp_tool(
        tool=serializer.validated_data["tool"],
        arguments=serializer.validated_data.get("arguments"),
        timeout=serializer.validated_data.get("timeout"),
    )
    return Response(data, status=status.HTTP_200_OK)
