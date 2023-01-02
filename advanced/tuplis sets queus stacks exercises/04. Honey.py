from collections import deque


def calculation(operator, number_1, number_2):
    if operator == "*":
        return abs(number_1 * number_2)
    elif operator == "+":
        return abs(number_1 + number_2)
    elif operator == "-":
        return abs(number_1 - number_2)
    elif operator == "/":
        if number_1 > 0:
            return abs(number_1 / number_2)
        else:
            return 0


bees = deque(int(x) for x in input().split())  # first
nectar = deque(int(x) for x in input().split())  # last
symbols = deque([x for x in input().split()])

collected = 0

while bees and nectar:
    current_bee = bees.popleft()
    current_nectar = nectar.pop()
    if current_nectar >= current_bee:
        current_symbol = symbols.popleft()
        result = calculation(current_symbol, current_bee, current_nectar)
        collected += result
    elif current_nectar < current_bee:
        bees.appendleft(current_bee)

print(f"Total honey made: {abs(collected)}")

if bees:
    print(f"Bees left: {', '.join(str(x) for x in bees)}")

if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")


# from collections import deque
#
# working_bees = deque(int(x) for x in input().split())
# nectar = deque(int(x) for x in input().split())
# operators = deque(x for x in input().split())
#
# nectar_all = 0

# symbols = {
#     "+": lambda a, b: a + b,
#     "-": lambda a, b: a - b,
#     "*": lambda a, b: a * b,
#     "/": lambda a, b: a / b,
# }

# while nectar and working_bees:
#     current_bee = working_bees[0]
#     current_nectar = nectar[-1]
#     if current_nectar >= current_bee:
#         current_symbol = operators.popleft()
#         if current_symbol == "+":
#             nectar_all += abs(current_bee + current_nectar)
#         if current_symbol == "-":
#             nectar_all += abs(current_bee - current_nectar)
#         if current_symbol == "*":
#             nectar_all += abs(current_bee * current_nectar)
#         if current_symbol == "/":
#             if current_bee > 0:
#                 nectar_all += abs(current_bee / current_nectar)
#         working_bees.popleft()
#         nectar.pop()
#     else:
#         nectar.pop()
#
# print(f"Total honey made: {nectar_all}")
#
# if working_bees:
#     print(f"Bees left: {', '.join(str(x) for x in working_bees)}")
# if nectar:
#     print(f"Nectar left: {', '.join(str(x) for x in nectar)}")
