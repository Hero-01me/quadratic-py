#Solve a quadratic equation using python

import cmath

print("General Form:- ax**2 + bx + c = 0")

a = int(input("Enter a (a != 0):"))
b = int(input("Enter b:"))
c = int(input("Enter c:"))

d = (b**2 - 4*a*c)

solution1 = (-b+cmath.sqrt(d))/(2*a)
solution2 = (-b-cmath.sqrt(d))/(2*a)

print("\n")
print(f"Results for equation, {a}x**2 + {b}x + {c} = 0, are :- \n")
if d > 0:
    print("Type of Roots: Two Distinct roots")
elif d < 0:
    print("Type of Roots: Two Complex roots")
elif d == 0:
    print("Type of Roots: Two Equal real roots")

print(f"The solutions are {solution1} and {solution2}")