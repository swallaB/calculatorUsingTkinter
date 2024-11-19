import math

class MathFunctions:

    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        if b != 0:
            return a / b
        else:
            return "ERROR! : DIVISION BY ZERO"

    def sq(self, a):
        return a ** 2

    def sqrt(self, a):
        if a >= 0:
            return math.sqrt(a)
        else:
            return "ERROR!: SQUARE ROOT OF NEGATIVE NUMBERS"

    def inverse(self, a):
        if a != 0:
            return 1 / a
        else:
            return "ERROR: CANNOT DIVIDE BY ZERO"

    def log(self, a, b):
        try:
            if a <= 0 or b <= 0 or b == 1:
                return "ERROR: INVALID BASE OR NUMBER FOR LOGARITHM"
            return math.log(a, b)
        except ValueError:
            return "ERROR: INVALID LOGARITHM OPERATION"

    def modulo(self, a, b):
        return a % b

    def ln(self, a):
        if a > 0:
            return math.log(a)
        else:
            return "ERROR: LN OF NON-POSITIVE NUMBERS"

    def factorial(self, a):
        if isinstance(a, int) and a >= 0:
            return math.factorial(a)
        else:
            return "ERROR: FACTORIAL IS ONLY DEFINED FOR NON-NEGATIVE INTEGERS"

    def absolute(self, a):
        return abs(a)

    def sin(self, a):
        return math.sin(math.radians(a))

    def cos(self, a):
        return math.cos(math.radians(a))

    def tan(self, a):
        try:
            return math.tan(math.radians(a))
        except ValueError:
            return "ERROR: TAN OF 90° + n*180° IS UNDEFINED"
