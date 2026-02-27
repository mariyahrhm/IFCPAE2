import unittest

from app import percentage

class TestQuizLogic(unittest.TestCase):

    def test_calculate_percentage_basic(self):
        self.assertEqual(percentage(3, 8), 10.0)

    def test_calculate_percentage_zero_total(self):
        self.assertEqual(percentage(0, 0), 100.0)

if __name__ == "__main__":
    unittest.main()