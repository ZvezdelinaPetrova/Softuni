from functools import reduce


def operate(operator, *args):
    if operator == "*":
        return reduce(lambda x, y: x * y, args)
    if operator == "/":
        return reduce(lambda x, y: x / y, args)
    if operator == "-":
        return reduce(lambda x, y: x - y, args)
    if operator == "+":
        return reduce(lambda x, y: x + y, args)


print(operate("+", 1, 5, 7))

print(operate("*", 3, 4))

# from collections import deque
#
#
# def operate(operator, *args):
#     if operator == "+":
#         return sum(args)
#     elif operator == "-":
#         new_list = deque(args)
#         first = new_list.popleft()
#         result = first
#         while new_list:
#             result -= new_list.popleft()
#         return result
#     elif operator == "*":
#         result = 1
#         for x in args:
#             result *= int(x)
#         return result
#     elif operator == "/":
#         new_list = deque(args)
#         first = new_list.popleft()
#         result = first
#         while new_list:
#             el = new_list.popleft()
#             if el != 0:
#                 result /= el
#         return result

