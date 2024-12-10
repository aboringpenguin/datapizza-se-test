import unittest

from llmclient import AnthropicMockClient, OpenAIMockClient


class TestLLMClient(unittest.TestCase):

    def test_openai_mock_client(self):
        client = OpenAIMockClient()
        client.load_model("text-davinci-003", temperature=0.5)
        response = client.generate_response("Ciao!", max_tokens=10)
        self.assertIn("response", response)

    def test_anthropic_mock_client(self):
        client = AnthropicMockClient()
        client.load_model("claude-v1", top_p=0.8)
        response = client.generate_response("Come stai?", stop_sequences=["\n"])
        self.assertIn("response", response)


if __name__ == '__main__':
    unittest.main()
