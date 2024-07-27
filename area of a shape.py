import math


def triangle_area(base, height):
    return (base * height) / 2


def quad_area(base, height):
    return base * height


def circle_area(radius):
    return math.pi * radius ** 2


print(triangle_area(4, 6))

shape = input("Which shape would you like to calculate? ")

if shape == "triangle" or shape == "Triangle":
    base = int(input("Base length (cm): "))
    height = int(input("Height length (cm): "))
    print(triangle_area(base, height))
elif shape == "circle" or shape == "Circle":
    radius = int(input("Radius (cm): "))
    print(circle_area(radius))
