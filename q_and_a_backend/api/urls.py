from django.urls import path
from .views import health, ask_question, mcp_invoke

urlpatterns = [
    path("health/", health, name="Health"),
    path("qa/ask/", ask_question, name="QAAsk"),
    path("mcp/invoke/", mcp_invoke, name="MCPInvoke"),
]
