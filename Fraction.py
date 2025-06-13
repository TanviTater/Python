from math import gcd

class Fraction(object):
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        assert type(numerator) == int and type(denominator) == int, "ints not used"
        self.numerator = numerator
        self.denominator = denominator
        self.reduce()

    def __str__(self):
        return str(self.numerator) + '/' + str(self.denominator)

    def __add__(self, other):
        top = self.numerator * other.denominator + other.numerator * self.denominator
        bottom = self.denominator * other.denominator
        return Fraction(top, bottom)

    def __sub__(self, other):
        top = self.numerator * other.denominator - other.numerator * self.denominator
        bottom = self.denominator * other.denominator
        return Fraction(top, bottom)

    def __mul__(self, other):
        top = self.numerator * other.numerator
        bottom = self.denominator * other.denominator
        return Fraction(top, bottom)

    def __truediv__(self, other):
        if other.numerator == 0:
            raise ZeroDivisionError("Cannot divide by zero fraction.")
        return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)

    def __float__(self):
        return self.numerator / self.denominator

    def inverse(self):
        if self.numerator == 0:
            raise ZeroDivisionError("Cannot invert a zero fraction.")
        return Fraction(self.denominator, self.numerator)

    def reduce(self):
        common = gcd(self.numerator, self.denominator)
        self.numerator //= common
        self.denominator //= common
        if self.denominator < 0:  # keep denominator positive
            self.numerator *= -1
            self.denominator *= -1

a = Fraction(1, 2)
b = Fraction(1, 3)
c = a + b

print("a + b =", c)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("float(c) =", float(c))
print("inverse(c) =", c.inverse())
print("c reduced =", c)  