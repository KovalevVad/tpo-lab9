from math import isqrt


def add(a, b):
    return a + b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Делитель равен нулю")
    return a / b


def is_prime_number(n: int) -> bool:
    if n < 2:
        return False
    return all(n % d != 0 for d in range(2, isqrt(n) + 1))
