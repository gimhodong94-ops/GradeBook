# ---------------------------------------------
# tests/test_utils.py
# ---------------------------------------------

import unittest
from gradebook.utils import mean, letter_grade

class TestUtils(unittest.TestCase):
    def test_mean(self):
        self.assertEqual(mean([10, 20, 30]), 20)
        self.assertEqual(mean([]), 0.0)

    def test_letter_grade(self):
        self.assertEqual(letter_grade(95), "A")
        self.assertEqual(letter_grade(85), "B")
        self.assertEqual(letter_grade(75), "C")
        self.assertEqual(letter_grade(65), "D")
        self.assertEqual(letter_grade(50), "F")

if __name__ == "__main__":
    unittest.main()
