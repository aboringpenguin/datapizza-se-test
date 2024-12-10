import unittest

from llmclient import OpenAIMockClient, AnthropicMockClient

class TestLLMClient(unittest.TestCase):

    def test_openai_mock_client(self):
        client = OpenAIMockClient()
        client.load_model("text-davinci-003", temperature=0.5)
        response = client.generate_response("Ciao!", "user-123", max_tokens=10)  # Aggiunto user_id
        self.assertIn("response", response)

    def test_anthropic_mock_client(self):
        client = AnthropicMockClient()
        client.load_model("claude-v1", top_p=0.8)
        response = client.generate_response("Come stai?", "user-456", stop_sequences=["\n"])  # Aggiunto user_id
        self.assertIn("response", response)


if __name__ == '__main__':
    unittest.main()
