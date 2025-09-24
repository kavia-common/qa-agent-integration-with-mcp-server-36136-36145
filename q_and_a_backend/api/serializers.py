from rest_framework import serializers


# PUBLIC_INTERFACE
class QuestionSerializer(serializers.Serializer):
    """Serializer for incoming question payload."""

    # Ocean Professional style metadata embedded for UI hints
    question = serializers.CharField(
        required=True,
        allow_blank=False,
        help_text="The natural-language question to answer.",
        style={
            "placeholder": "Ask your question...",
            "base_color": "#2563EB",
            "accent_color": "#F59E0B",
        },
    )
    context = serializers.CharField(
        required=False,
        allow_blank=True,
        help_text="Optional context to bias or ground the answer.",
        style={"background": "#f9fafb"},
    )
    use_mcp = serializers.BooleanField(
        required=False,
        default=False,
        help_text="Route question to MCP server tools when true.",
        style={"switch_color": "#2563EB"},
    )


# PUBLIC_INTERFACE
class AnswerSerializer(serializers.Serializer):
    """Serializer for outgoing answer payload."""

    answer = serializers.CharField(help_text="Generated answer text.")
    source = serializers.CharField(
        help_text="Indicates where the answer was produced: 'local' or 'mcp'."
    )
    meta = serializers.DictField(
        child=serializers.JSONField(),
        required=False,
        help_text="Optional metadata, e.g., timing, tool usage, and style hints.",
    )


# PUBLIC_INTERFACE
class MCPInvokeSerializer(serializers.Serializer):
    """Serializer for requesting MCP tool invocation."""

    tool = serializers.CharField(
        help_text="MCP tool name to invoke.",
        style={"base_color": "#2563EB"},
    )
    arguments = serializers.DictField(
        child=serializers.JSONField(),
        required=False,
        help_text="Arguments passed to the tool.",
    )
    timeout = serializers.IntegerField(
        required=False,
        min_value=1,
        max_value=120,
        default=30,
        help_text="Timeout in seconds for MCP request.",
    )
