from math import floor
from collections import deque

text = deque(input().split())

main = ["red", "yellow", "blue"]
secondary = ["orange", "purple", "green"]

colors_found = []

while text:
    if len(text) == 1:
        last_string = text.pop()
        if last_string in main:
            colors_found.append(last_string)
        elif last_string in secondary:
            colors_found.append(last_string)
    else:
        first = text.popleft()
        second = text.pop()
        result = first + second
        reversed_result = second + first
        if result in main or result in secondary:
            colors_found.append(result)
        elif reversed_result in main or reversed_result in secondary:
            colors_found.append(reversed_result)
        else:
            middle = floor(len(text) / 2)
            first_to_insert = first[:-1]  # Взима думата без последния символ
            second_to_insert = second[:-1]
            if first_to_insert:
                text.insert(middle, first_to_insert)
            if second_to_insert:
                text.insert(middle, second_to_insert)

for color in colors_found:
    if color in secondary:
        if color == "orange":
            if "red" in colors_found and "yellow" in colors_found:
                continue
            else:
                colors_found.remove(color)
        elif color == "purple":
            if "red" in colors_found and "blue" in colors_found:
                continue
            else:
                colors_found.remove(color)
        elif color == "green":
            if "yellow" in colors_found and "blue" in colors_found:
                continue
            else:
                colors_found.remove(color)

print(colors_found)


# from collections import deque
#
# text = deque(input().split())
#
# main_colors = ["red", "yellow", "blue"]
# secondary_colors = ["orange", "purple", "green"]
#
# collected_colors = []
#
# while text:
#     left = text.popleft()
#     right = text.pop() if text else ''
#     result = left + right
#     if result in main_colors or result in secondary_colors:
#         collected_colors.append(result)
#         continue
#     new_result = right + left
#     if new_result in main_colors or new_result in secondary_colors:
#         collected_colors.append(new_result)
#     else:
#         left = left[:-1]
#         right = right[:-1]
#         if left:
#             where_to_insert = len(text) // 2
#             text.insert(where_to_insert, left)
#         if right:
#             where_to_insert = len(text) // 2
#             text.insert(where_to_insert, right)
#
#
# required_colors = {
#     "orange": ["red", "yellow"],
#     "purple": ["red", "blue"],
#     "green": ["blue", "yellow"]
# }
#
# for color in collected_colors:
#     if color in main_colors:
#         continue
#     color_one, color_two = required_colors[color]
#     if not(color_one in collected_colors) or not (color_two in collected_colors):
#         collected_colors.remove(color)
# print(collected_colors)