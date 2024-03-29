import unittest
import calc


class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(10, -3), 7)
        self.assertEqual(calc.add(-4, -6), -10)
        self.assertEqual(calc.add(0, -1), -1)

    def test_subtract(self):
        self.assertEqual(calc.subtract(5, 9), -4)
        self.assertEqual(calc.subtract(-3, 9), -12)
        self.assertEqual(calc.subtract(-3, -9), 6)
        self.assertEqual(calc.subtract(3, -9), 12)

    def test_multiply(self):
        self.assertEqual(calc.multiply(5, 9), 45)
        self.assertEqual(calc.multiply(-3, 9), -27)
        self.assertEqual(calc.multiply(-3, -9), 27)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-9, 3), -3)
        self.assertEqual(calc.divide(-9, 3), -3)
        self.assertEqual(calc.divide(-9, -3), 3)
        with self.assertRaises(ValueError):
            calc.divide(10, 0)


if __name__ == "__main__":
    unittest.main()
