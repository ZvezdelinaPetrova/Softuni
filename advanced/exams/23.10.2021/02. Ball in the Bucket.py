def valid_index(one, two):
    if 0 <= one < row and 0 <= two < row:
        return True


def check_for_success(res):
    if 100 <= res <= 199:
        return "Football"
    elif 200 <= res <= 299:
        return "Teddy Bear"
    elif 300 <= res <= 399:
        return "Lego Construction Set"


row = 6

matrix = []

for r in range(row):
    matrix.append(input().split())

won = ""
result = 0
price_won = False

for _ in range(3):
    text = input()
    o = text[1:-1]
    one, two = o.split(", ")
    index_1 = int(one)
    index_2 = int(two)
    if valid_index(index_1, index_2):
        if matrix[index_1][index_2] == "B":
            matrix[index_1][index_2] = "-"
            for x in range(row):
                if matrix[x][index_2] == "-":
                    continue
                else:
                    current_sum = int(matrix[x][index_2])
                    result += current_sum

        elif matrix[index_1][index_2] == "-":
            continue


if check_for_success(result):
    price_won = True
    found = check_for_success(result)
    won = found

if price_won:
    print(f"Good job! You scored {result} points, and you've won {won}.")
else:
    print(f"Sorry! You need {100 - result} points more to win a prize.")

# def valid_index(r, c, rows):
#     return 0 <= r < rows and 0 <= c < rows
#
#
# def row_up(rol, col, rows):
#     return rol - 1, col
#
#
# def row_down(rol, col, rows):
#     return rol + 1, col
#
#
# rows = 6
# matrix = []
# points = 0
# hit_toys = []
#
# for r in range(rows):
#     matrix.append([x for x in input().split(" ")])
#
# for _ in range(3):
#     throw_info = input()
#     stripped_info = throw_info[1:len(throw_info) - 1]
#     row, col = int(stripped_info[0]), int(stripped_info[-1])
#     current_el = matrix[row][col]
#     if valid_index(row, col, rows):
#         if current_el == "B":
#             matrix[row][col] = "-"
#             current_row, current_col = row, col
#             for _ in range(rows):
#                 next_row, next_col = row_up(current_row, current_col, rows)
#                 if valid_index(next_row, next_col, rows):
#                     if matrix[next_row][next_col].isdigit():
#                         points += int(matrix[next_row][next_col])
#                     current_row, current_col = next_row, next_col
#                 else:
#                     break
#
#             current_row, current_col = row, col
#             for _ in range(rows):
#                 next_row, next_col = row_down(current_row, current_col, rows)
#                 if valid_index(next_row, next_col, rows):
#                     if matrix[next_row][next_col].isdigit():
#                         points += int(matrix[next_row][next_col])
#                     current_row, current_col = next_row, next_col
#                 else:
#                     break
#         elif matrix[row][col] == "-":
#             continue
#
# if 100 <= points < 200:
#     hit_toys.append("Football")
# if 200 <= points < 300:
#     hit_toys.append("Teddy Bear")
# if 300 <= points:
#     hit_toys.append("Lego Construction Set")
#
# if not hit_toys:
#     print(f"Sorry! You need {100 - points} points more to win a prize.")
# else:
#     for el in hit_toys:
#         print(f"Good job! You scored {points} points, and you've won {el}.")