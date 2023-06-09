import unittest

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b


class CalculatorTest(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        result = self.calculator.add(2, 3)
        self.assertEqual(result, 5)

    def test_subtract(self):
        result = self.calculator.subtract(5, 3)
        self.assertEqual(result, 2)

    def test_multiply(self):
        result = self.calculator.multiply(4, 3)
        self.assertEqual(result, 12)

    def test_divide(self):
        result = self.calculator.divide(10, 2)
        self.assertEqual(result, 5)

        with self.assertRaises(ValueError):
            self.calculator.divide(10, 0)

if __name__ == '__main__':
    unittest.main()
