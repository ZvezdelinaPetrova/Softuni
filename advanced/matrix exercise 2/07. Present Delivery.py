def valid_index(r, c):
    return 0 <= r < size and 0 <= c < size


directions = {
    'right': lambda r, c: (r, c + 1),
    'left': lambda r, c: (r, c - 1),
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c)
}

presents = int(input())
size = int(input())

matrix = []

s_row = 0
s_col = 0
nice_kids = 0


for row in range(size):
    row_elements = list(input().split())
    matrix.append(row_elements)
    for col in range(size):
        el = row_elements[col]
        if el == 'S':
            s_row, s_col = row, col
        elif el == "V":
            nice_kids += 1

initial_kids = nice_kids
command = input()

while command != "Christmas morning" and presents > 0:
    direction = command
    next_row, next_col = directions[direction](s_row, s_col)
    if valid_index(next_row, next_col):
        matrix[s_row][s_col] = "-"
        if matrix[next_row][next_col] == "X":
            matrix[next_row][next_col] = "S"
            s_row, s_col = next_row, next_col
        elif matrix[next_row][next_col] == "V":
            matrix[next_row][next_col] = "S"
            presents -= 1
            nice_kids -= 1  # da proverya dali sa 0- nice kids i ako da break
            s_row, s_col = next_row, next_col
        elif matrix[next_row][next_col] == "C":
            matrix[next_row][next_col] = "S"
            for d in directions:
                index_1, index_2 = directions[d](next_row, next_col)
                if matrix[index_1][index_2] == "V":
                    presents -= 1
                    nice_kids -= 1
                    matrix[index_1][index_2] = "-"
                    if presents <= 0:
                        break
                elif matrix[index_1][index_2] == "X":
                    matrix[index_1][index_2] = "-"
                    presents -= 1
                    if presents <= 0:
                        break
        else:
            matrix[next_row][next_col] = "S"
            s_row, s_col = next_row, next_col
    else:
        break
    if presents <= 0:
        break

    command = input()

if presents == 0 and nice_kids > 0:
    print(f"Santa ran out of presents!")

for l in matrix:
    print(f"{' '.join(x for x in l)}")

if nice_kids == 0:
    print(f"Good job, Santa! {initial_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids} nice kid/s.")

# def valid_index(r, c, rows):
#     return 0 <= r < rows and 0 <= c < rows
#
#
# def move_to_next_position(rol, col, direction):
#     if direction == "up":
#         return rol - 1, col
#     if direction == "down":
#         return rol + 1, col
#     if direction == "right":
#         return rol, col + 1
#     if direction == "left":
#         return rol, col - 1
#
#
# def cells_around_santa(rol, col):
#     result_list = []
#     result_list.append([rol - 1, col])
#     result_list.append([rol + 1, col])
#     result_list.append([rol, col + 1])
#     result_list.append([rol, col - 1])
#     return result_list
#
#
# presents_all = int(input())
# rows = int(input())
#
# matrix = []
#
# santa_row = 0
# santa_col = 0
# nice_kids = 0
# result_list = []
#
# for row in range(rows):
#     row_elements = list(input().split())
#     matrix.append(row_elements)
#     for col in range(rows):
#         el = row_elements[col]
#         if el == 'S':
#             santa_row, santa_col = row, col
#         elif el == "V":
#             nice_kids += 1
#
# initial_nice_kids = nice_kids
#
# command = input()
#
# presents_finished = False
#
# while command != "Christmas morning":
#     direction = command
#     current_row, current_col = santa_row, santa_col
#     next_row, next_col = move_to_next_position(current_row, current_col, direction)
#     if valid_index(next_row, next_col, rows):
#         if matrix[next_row][next_col] == "C":
#             result_list = cells_around_santa(next_row, next_col)
#             for row, col in result_list:
#                 if matrix[row][col] == "V":
#                     nice_kids -= 1
#                     presents_all -= 1
#                     matrix[row][col] = "-"
#                     if presents_all <= 0:
#                         presents_finished = True
#                         break
#                 elif matrix[row][col] == "X":
#                     presents_all -= 1
#                     matrix[row][col] = "-"
#                     if presents_all <= 0:
#                         presents_finished = True
#                         break
#             matrix[next_row][next_col] = "S"
#             matrix[santa_row][santa_col] = "-"
#             santa_row, santa_col = next_row, next_col
#         elif matrix[next_row][next_col] == "V":
#             presents_all -= 1
#             nice_kids -= 1
#             matrix[next_row][next_col] = "S"
#             matrix[santa_row][santa_col] = "-"
#             santa_row, santa_col = next_row, next_col
#             if presents_all <= 0:
#                 break
#         elif matrix[next_row][next_col] == "X":
#             matrix[next_row][next_col] = "S"
#             matrix[santa_row][santa_col] = "-"
#             santa_row, santa_col = next_row, next_col
#         elif matrix[next_row][next_col] == "-":
#             matrix[next_row][next_col] = "S"
#             matrix[santa_row][santa_col] = "-"
#             santa_row, santa_col = next_row, next_col
#     if presents_finished:
#         break
#     command = input()
#
#
# if (presents_all <= 0) and (nice_kids > 0):
#     print(f"Santa ran out of presents!")
#
#
# for row in matrix:
#     print(' '.join(row))
#
# if nice_kids <= 0:
#     print(f"Good job, Santa! {initial_nice_kids} happy nice kid/s.")
# else:
#     print(f"No presents for {nice_kids} nice kid/s.")


