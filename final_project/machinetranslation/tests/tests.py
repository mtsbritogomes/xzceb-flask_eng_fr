import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):

    def test_english_to_french(self):
        """
        Test for translation of "Hello" to "Bonjour"
        and "Goodbye" to "Au revoir"
        """
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertEqual(english_to_french("Goodbye"), "Au revoir")

    def test_french_to_english(self):
        """
        Test for translation of "Bonjour" to "Hello"
        and "Au revoir" to "Goodbye"
        """
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertEqual(french_to_english("Au revoir"), "Goodbye")

    def test_null_input(self):
        """
        Test for null input for translate
        """
        self.assertEqual(english_to_french(None), None)
        self.assertEqual(french_to_english(None), None)

if __name__ == '__main__':
    unittest.main()
