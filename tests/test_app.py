import unittest

from app import percentage

class TestQuizLogic(unittest.TestCase):
    def test_calculate_percentage(self):
        self.assertEqual(percentage(4, 8), 60.00)

if __name__ == "__main__":
    unittest.main()