from fractions import Fraction
from functools import reduce
from fractions import gcd


def product(fracs):
    t = Fraction(reduce(lambda x, y: Fraction((x.numerator * y.numerator), (x.denominator * y.denominator)), fracs))
    return t.numerator, t.denominator


if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)
