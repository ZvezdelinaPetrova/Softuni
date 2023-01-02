from collections import deque

text = deque([x for x in input()])
opening_s = deque() # pop


new_dict = {
    "(": ")",
    "{": "}",
    "[": "]"
}

failed = False

if len(text) % 2 == 1:
    print("NO")
    exit()

while text:
    current_symbol = text.popleft()
    if current_symbol in "({[":
        opening_s.append(current_symbol)
        continue
    else:
        closing_symbol = current_symbol
        last_opening = opening_s.pop()
        if new_dict[last_opening] == closing_symbol:
            continue
        else:
            failed = True
            break

if failed:
    print("NO")
else:
    print("YES")


#
#
# data = input()
#
# symbols = []
#
# for j in data:
#     symbols.append(j)
#
# opening_list = []
# closing_list = []
# balanced = True
#
# if len(symbols) % 2 == 1:
#     balanced = False
#
# while symbols:
#     current_symbol = symbols[0]
#     if current_symbol in "({[":
#         opening_list.append(current_symbol)
#         symbols.remove(current_symbol)
#     elif current_symbol in ")}]":
#         if opening_list:
#             last_opening_symbol = opening_list[-1]
#             if last_opening_symbol == "(" and current_symbol == ")":
#                 opening_list.pop()
#                 symbols.remove(current_symbol)
#             elif last_opening_symbol == "{" and current_symbol == "}":
#                 opening_list.pop()
#                 symbols.remove(current_symbol)
#             elif last_opening_symbol == "[" and current_symbol == "]":
#                 opening_list.pop()
#                 symbols.remove(current_symbol)
#             else:
#                 balanced = False
#                 break
#         else:
#             break
# if balanced:
#     print("YES")
# else:
#     print("NO")
