class Rational(object):
    def __init__(self, numer: int, denom: int):
        self._prepare_args(numer, denom)

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        numer = self.numer * other.denom + other.numer * self.denom
        denum = self.denom * other.denom
        return Rational(numer, denum)

    def __sub__(self, other):
        return Rational(self.numer, self.denom) + Rational(-other.numer, other.denom)

    def __mul__(self, other):
        numer = self.numer * other.numer
        denum = self.denom * other.denom
        return Rational(numer, denum)

    def __truediv__(self, other):
        return Rational(self.numer, self.denom) * Rational(other.denom, other.numer)

    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        return Rational(self.numer ** power, self.denom ** power)

    def __rpow__(self, base):
        return base ** (self.numer / self.denom)

    def _prepare_args(self, numer, denom):
        gcd = self._find_gcd(numer, denom)
        self.numer, self.denom = self._negativity_check(int(numer / gcd), int(denom / gcd))

    @staticmethod
    def _negativity_check(num_a, num_b):
        if num_b < 0:
            num_a *= -1
            num_b *= -1
        return num_a, num_b

    @staticmethod
    def _find_gcd(num_a, num_b):
        for i in range(max(num_a, num_b), 0, -1):
            if num_a % i == 0 and num_b % i == 0:
                return i
        return 1
