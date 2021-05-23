class Fraction:

    def __init__(self, delit, znam):
        self.delit = delit
        self.znam = znam


    def __add__(self, other):
        delit = self.delit + other.delit
        znam = self.znam = other.znam
        return Fraction(delit,znam)

    def __mul__(self, other):
        delit = self.delit * other.delit
        znam = self.znam * other.znam
        return Fraction(delit, znam)

    def __truediv__(self, other):
        delit = self.delit * other.znam
        znam = self.znam * other.delit
        return Fraction(delit, znam)

    def __sub__(self, other):
        delit = self.delit - other.delit
        znam = self.znam = other.znam
        return Fraction(delit, znam)

m = Fraction(3,4)
k = Fraction(2,4)
plus = m + k
mul = m * k
minus = m - k
trudiv = m /k

print(plus.delit)
print('-')
print(plus.znam)

print(mul.delit)
print('-')
print(mul.znam)

print(minus.delit)
print('-')
print(minus.znam)

print(trudiv.delit)
print('-')
print(trudiv.znam)