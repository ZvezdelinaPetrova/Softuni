def multiply(*args):
    result = 1
    for x in args:
        result *= x
    return result


print(multiply(1, 4, 5))
print(multiply(4, 5, 6, 1, 3))
print(multiply(2, 0, 1000, 5000))

# def multiply(*args):
#     new_list = args
#     result = 1
#     for x in new_list:
#         result *= x
#     return result
