from rest_framework.test import APITestCase
from django.urls import reverse


class HealthTests(APITestCase):
    def test_health(self):
        url = reverse("Health")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.get("message"), "Server is up!")


class QATests(APITestCase):
    def test_local_answer(self):
        url = reverse("QAAsk")
        payload = {"question": "Hello?", "use_mcp": False}
        response = self.client.post(url, payload, format="json")
        self.assertEqual(response.status_code, 200)
        self.assertIn("answer", response.data)
        self.assertEqual(response.data.get("source"), "local")


class MCPInvokeTests(APITestCase):
    def test_mcp_invoke_validation(self):
        url = reverse("MCPInvoke")
        # missing tool name
        payload = {"arguments": {"x": 1}}
        response = self.client.post(url, payload, format="json")
        self.assertEqual(response.status_code, 400)
