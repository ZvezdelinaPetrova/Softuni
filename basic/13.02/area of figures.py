from math import pi

figure = input()

if figure == "square":
    size = float(input())
    square_area = size * size
    print(f"{square_area:.3f}")


if figure == "rectangle":
    size = float(input())
    size2 = float(input())
    rectangle_area = size * size2
    print(rectangle_area)


if figure == "circle":
    size = float(input())
    circle_area = pi * size * size
    print(circle_area)

if figure == "triangle":
    size = float(input())
    size2 = float(input())
    triangle_area = size * size2 / 2
    print(triangle_area)





