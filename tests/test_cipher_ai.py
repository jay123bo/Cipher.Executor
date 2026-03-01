import unittest

from cipher_ai import CipherAI


class CipherAITests(unittest.TestCase):
    def test_fallback_without_client(self):
        bot = CipherAI(client=None)
        reply = bot.reply("hello")
        self.assertIn("Local mode", reply)
        self.assertEqual(bot.history[0]["role"], "user")
        self.assertEqual(bot.history[1]["role"], "assistant")


if __name__ == "__main__":
    unittest.main()
