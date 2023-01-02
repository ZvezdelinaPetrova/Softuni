def even_odd(*args):
    word = args[-1]
    elements = args[:len(args) - 1]
    result = []
    if word == "even":
        result = [int(x) for x in elements if x % 2 == 0]
    else:
        result = [int(x) for x in elements if x % 2 == 1]

    return result


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))

# def even_odd(*elements):
#     if elements[-1] == 'even':
#         return list(filter(lambda x: x % 2 == 0, elements[:-1]))
#     return list(filter(lambda x: x % 2 == 1, elements[:-1]))
#
#
# print(even_odd(1, 2, 3, 4, 5, 6, "even"))
# print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))