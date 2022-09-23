from numpy import sqrt
from sympy.plotting import *
from sympy import Symbol


# ax^2 +bx + c
def zeros(a, b, c):
    D = sqrt(b * b - 4 * a * c)
    x1 = (-b + D) / (2 * a)
    x2 = (-b - D) / (2 * a)
    print("The first root is: ", x1)
    print("The second root is: ", x2)


if __name__ == "__main__":
    print("Welcome to the quadratic calculator")
    a = input("Enter a: ")
    b = input("Enter b: ")
    c = input("Enter c: ")

    zeros(float(a), float(b), float(c))
