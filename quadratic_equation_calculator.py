from numpy import sqrt
from sympy.plotting import *
from sympy import Symbol


# ax^2 +bx + c
# quadratic formula calculator
def find_zeros(a, b, c):
    discriminant = sqrt(b * b - 4 * a * c)
    x1 = (-b + discriminant) / (2 * a)
    x2 = (-b - discriminant) / (2 * a)
    return x1, x2


# linear
# given two points, returns linear equation of line passing through those points
def linear(point1, point2):
    x = Symbol("x")
    a, b = point1
    c, d = point2
    s = slope(a, b, c, d)
    # Use Point-Slope Form
    return s * (x - a) + b


# can determine if two lines are perpendicaular if slopes are
# negative reciprocoal of each other
def are_perpendicular(m1, m2):
    negative_rec = -1 * (1 / m2)
    return m1 == negative_rec


def slope(a, b, c, d):
    # Compute the slope
    s = (d - b) / (c - a)
    return s


def print_graph(a, b, c):
    x = Symbol("x")
    plot(a * x**2 + b * x + c)


if __name__ == "__main__":
    # print("Welcome to the quadratic calculator")
    # a = input("Enter a: ")
    # b = input("Enter b: ")
    # c = input("Enter c: ")

    # r1, r2 = find_zeros(float(a), float(b), float(c))
    # print("The first root is: ", r1)
    # print("The second root is: ", r2)

    # print_graph(float(a), float(b), float(c))

    print("Welcome to the linear function creator")
    a = input("Enter a: ")
    b = input("Enter b: ")
    c = input("Enter c: ")
    d = input("Enter d: ")

    linear_func = linear((float(a), float(b)), (float(c), float(d)))
    print(linear_func)
    plot(linear_func)

    # print_graph(float(a), float(b), float(c))
