from math import floor
from collections import deque


def calculation(operator, number_1, number_2):
    if operator == "*":
        return number_1 * number_2
    elif operator == "+":
        return number_1 + number_2
    elif operator == "-":
        return number_1 - number_2
    elif operator == "/":
        return floor(number_1 / number_2)


text = deque([x for x in input().split()])
symbols = ["*", "+", "-", "/"]

numbers_result = deque()

while text:
    current_element = text.popleft()
    if current_element in symbols:
        while len(numbers_result) > 1:
            n_1 = numbers_result.popleft()
            n_2 = numbers_result.popleft()
            result = calculation(current_element, n_1, n_2)
            numbers_result.appendleft(result)
    else:
        current_element = int(current_element)
        numbers_result.append(current_element)

print(*numbers_result)



# from collections import deque
#
# text = deque(input().split())
#
# operators = {
#     "*": lambda a, b: a * b,
#     "+": lambda a, b: a + b,
#     "-": lambda a, b: a - b,
#     "/": lambda a, b: a // b
# }
#
# numbers = deque()
#
# for ch in text:
#     if ch in operators:
#         action = operators[ch]
#         result = numbers.popleft()
#         while numbers:
#             second_number = numbers.popleft()
#             result = action(result, second_number)
#         numbers.append(result)
#     else:
#         numbers.append(int(ch))
#
# print(*numbers)