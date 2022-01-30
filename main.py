from fractions import Fraction
a = int(input("2 "))
b = int(input("1 "))
c = int(input("0 "))
a1 = (-1 * b + (b**2-4*a*c)**0.5)
a2 = (-1 * b - (b**2-4*a*c)**0.5)
a3 = 2 * a
print(Fraction(Fraction(a1), Fraction(a3)))
print(Fraction(Fraction(a2), Fraction(a3)))