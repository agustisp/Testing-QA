import unittest
from main import add, subtract, multiply, divide

class TestCalculatorFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(3.5, 2.5), 6.0)

    def test_subtract(self):
        self.assertEqual(subtract(3, 2), 1)
        self.assertEqual(subtract(0, 0), 0)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(2.5, 1.5), 1.0)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(0, 3), 0)
        self.assertEqual(multiply(4, 0), 0)
        self.assertEqual(multiply(2.5, 1.5), 3.75)

    def test_divide(self):
        self.assertEqual(divide(6, 3), 2.0)
        self.assertEqual(divide(0, 3), 0.0)
        self.assertEqual(divide(1, 0), "Tidak dapat membagi oleh nol")
        self.assertEqual(divide(2.5, 1.25), 2.0)

if __name__ == '__main__':
    unittest.main()