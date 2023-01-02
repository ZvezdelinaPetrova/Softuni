def valid_index(r, c):
    return 0 <= r < size and 0 <= c < size


directions = {
    'right': lambda r, c: (r, c + 1),
    'left': lambda r, c: (r, c - 1),
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c)
}

size = int(input())

matrix = []

a_row = 0
a_col = 0

for row in range(size):
    row_elements = list(input().split())
    matrix.append(row_elements)
    for col in range(size):
        el = row_elements[col]
        if el == 'A':
            a_row, a_col = row, col

collected = 0
did_not_succeed = False
went_out = False
matrix[a_row][a_col] = "*"
while collected < 10:
    command = input()
    a_row, a_col = directions[command](a_row, a_col)
    if valid_index(a_row, a_col):
        if matrix[a_row][a_col] == ".":
            matrix[a_row][a_col] = "*"
        elif matrix[a_row][a_col] == "R":
            did_not_succeed = True
            matrix[a_row][a_col] = "*"
            break
        elif matrix[a_row][a_col].isdigit():
            collected += int(matrix[a_row][a_col])
            matrix[a_row][a_col] = "*"
    else:
        went_out = True
        break


if went_out or did_not_succeed:
    print(f"Alice didn't make it to the tea party.")

if collected >= 10:
    print(f"She did it! She went to the party.")

for l in matrix:
    print(f"{' '.join(str(x) for x in l)}")

# def valid_index(r, c, rows):
#     return 0 <= r < rows and 0 <= c < rows
#
#
# def get_next_position(rol, col, direction):
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
# rows = int(input())
#
# matrix = []
#
# alice_row = 0
# alice_col = 0
#
# for row in range(rows):
#     row_elements = list(input().split())
#     matrix.append(row_elements)
#     for col in range(rows):
#         el = row_elements[col]
#         if el == 'A':
#             alice_row, alice_col = row, col
#
# tea = 0
# out_of_range = False
# rabbit_trap = False
#
# matrix[alice_row][alice_col] = "*"
#
# while True:
#     direction = input()
#     next_row, next_col = get_next_position(alice_row, alice_col, direction)
#
#     if not valid_index(next_row, next_col, rows):
#         out_of_range = True
#         break
#
#     if valid_index(next_row, next_col, rows):
#         if matrix[next_row][next_col] == "R":
#             matrix[next_row][next_col] = '*'
#             rabbit_trap = True
#             break
#         if matrix[next_row][next_col] == ".":
#             alice_row, alice_col = next_row, next_col
#             matrix[next_row][next_col] = '*'
#             continue
#         if matrix[next_row][next_col].isdigit():
#             tea += int(matrix[next_row][next_col])
#             alice_row, alice_col = next_row, next_col
#             matrix[next_row][next_col] = '*'
#             if tea >= 10:
#                 break
#         if matrix[next_row][next_col] == "*":
#             alice_row, alice_col = next_row, next_col
#
# if tea >= 10:
#     print("She did it! She went to the party.")
# if rabbit_trap or out_of_range:
#     print("Alice didn't make it to the tea party.")
#
# for row in matrix:
#     print(' '.join(row))