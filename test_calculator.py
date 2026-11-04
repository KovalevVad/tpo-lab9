import unittest
from calculator import add, divide, is_prime_number


class CalculatorTests(unittest.TestCase):
    def test_add(self):
        for a, b, expected in [(2, 3, 5), (-2, 2, 0), (0, 0, 0), (0.5, 1, 1.5)]:
            with self.subTest(a=a, b=b):
                self.assertEqual(add(a, b), expected)

    def test_divide(self):
        for a, b, expected in [(8, 2, 4), (1, 4, 0.25), (0, 3, 0), (6, -2, -3)]:
            with self.subTest(a=a, b=b):
                self.assertEqual(divide(a, b), expected)

    def test_zero_divisor(self):
        for a in (0, 1, -5):
            with self.subTest(a=a):
                with self.assertRaises(ZeroDivisionError):
                    divide(a, 0)

    def test_primes(self):
        for n in (-5, 0, 1, 2, 3, 4, 17, 49):
            with self.subTest(n=n):
                self.assertEqual(is_prime_number(n), n in (2, 3, 17))
