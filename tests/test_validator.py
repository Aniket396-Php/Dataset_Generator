import unittest
from src.validator import Validator

class TestValidator(unittest.TestCase):
    def test_valid_pair(self):
        pair = {
            "question": "Who was Ragnar Lothbrok?",
            "answer": "Ragnar Lothbrok was a legendary Norse hero and king known for his daring raids on England and France."
        }
        self.assertTrue(Validator.validate_pair(pair))

if __name__ == '__main__':
    unittest.main()
