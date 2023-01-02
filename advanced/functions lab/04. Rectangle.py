def rectangle(length, width):
    if not isinstance(length, int) or not isinstance(width, int):
        return f"Enter valid values!"

    result = ""
    area_result = area(length, width)
    per_result = perimeter(length, width)
    result += f"Rectangle area: {area_result}" + "\n"
    result += f"Rectangle perimeter: {per_result}" + "\n"
    return result.strip()


def area(length, width):
    return length * width


def perimeter(length, width):
    result = 2 * (length + width)
    return result


print(rectangle(2, 10))
print(rectangle('2', 10))

# може да се правят функции във функция, но вътрешната не е достъпна отвън