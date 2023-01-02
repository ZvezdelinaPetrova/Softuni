from collections import deque
row = int(input())

matrix = []

directions = deque(x for x in input().split())

for _ in range(row):
    matrix.append([x for x in input().split()])


def valid_index(one, two):
    if 0 <= one < row and 0 <= two < row:
        return True


def next_position(direction, ro, col):
    if direction == "left":
        next_r, next_c = ro, col - 1
        return next_r, next_c
    if direction == "right":
        next_r, next_c = ro, col + 1
        return next_r, next_c
    if direction == "up":
        next_r, next_c = ro - 1, col
        return next_r, next_c
    if direction == "down":
        next_r, next_c = ro + 1, col
        return next_r, next_c


coal = 0
collected = 0
miner_row = ""
miner_col = ""
stepped_on_end = False

for r in range(row):
    for c in range(row):
        if matrix[r][c] == "c":
            coal += 1
        elif matrix[r][c] == "s":
            miner_row, miner_col = r, c

while directions:
    current_direction = directions.popleft()
    next_row, next_col = next_position(current_direction, miner_row, miner_col)
    if not valid_index(next_row, next_col):
        continue
    miner_row, miner_col = next_row, next_col
    if matrix[miner_row][miner_col] == "c":
        matrix[miner_row][miner_col] = "*"
        collected += 1
        if coal == collected:
            print(f"You collected all coal! ({miner_row}, {miner_col})")
            exit()
    elif matrix[miner_row][miner_col] == "e":
        print(f"Game over! ({miner_row}, {miner_col})")
        stepped_on_end = True
        break

    matrix[miner_row][miner_col] = "s"

if not stepped_on_end:
    print(f"{coal - collected} pieces of coal left. ({miner_row}, {miner_col})")

# from collections import deque
#
#
# def is_valid_index(rol, col, row):
#     if rol < 0 or col < 0 or rol >= row or col >= row:
#         return False
#     return True
#
#
# rows = int(input())
#
# directions = deque(input().split())
#
# matrix = []
#
# for _ in range(rows):
#     matrix.append([x for x in input().split()])
#
#
# count = 0
#
# start_row = 0
# start_col = 0
#
# for r in range(rows):
#     for c in range(rows):
#         current_element = matrix[r][c]
#         if current_element == "c":
#             count += 1
#         elif current_element == "s":
#             start_row = r
#             start_col = c
#
# died = False
#
# while directions and not died:
#     current_command = directions.popleft()
#     if current_command == "up":
#         if is_valid_index(start_row - 1, start_col, rows):
#             if matrix[start_row - 1][start_col] == "e":
#                 died = True
#                 start_row, start_col = start_row - 1, start_col
#                 break
#             elif matrix[start_row - 1][start_col] == "*":
#                 start_row, start_col = start_row - 1, start_col
#             elif matrix[start_row - 1][start_col] == "c":
#                 matrix[start_row - 1][start_col] = "*"
#                 start_row, start_col = start_row - 1, start_col
#                 count -= 1
#                 if count <= 0:
#                     break
#
#     elif current_command == "down":
#         if is_valid_index(start_row + 1, start_col, rows):
#             if matrix[start_row + 1][start_col] == "e":
#                 died = True
#                 start_row, start_col = start_row + 1, start_col
#                 break
#             elif matrix[start_row + 1][start_col] == "*":
#                 start_row, start_col = start_row + 1, start_col
#             elif matrix[start_row + 1][start_col] == "c":
#                 matrix[start_row + 1][start_col] = "*"
#                 start_row, start_col = start_row + 1, start_col
#                 count -= 1
#                 if count <= 0:
#                     break
#
#     elif current_command == "right":
#         if is_valid_index(start_row, start_col + 1, rows):
#             if matrix[start_row][start_col + 1] == "e":
#                 died = True
#                 start_row, start_col = start_row, start_col + 1
#                 break
#             elif matrix[start_row][start_col + 1] == "*":
#                 start_row, start_col = start_row, start_col + 1
#             elif matrix[start_row][start_col + 1] == "c":
#                 matrix[start_row][start_col + 1] = "*"
#                 start_row, start_col = start_row, start_col + 1
#                 count -= 1
#                 if count <= 0:
#                     break
#
#     elif current_command == "left":
#         if is_valid_index(start_row, start_col - 1, rows):
#             if matrix[start_row][start_col - 1] == "e":
#                 died = True
#                 start_row, start_col = start_row, start_col - 1
#                 break
#             elif matrix[start_row][start_col - 1] == "*":
#                 start_row, start_col = start_row, start_col - 1
#             elif matrix[start_row][start_col - 1] == "c":
#                 matrix[start_row][start_col - 1] = "*"
#                 start_row, start_col = start_row, start_col - 1
#                 count -= 1
#                 if count <= 0:
#                     break
#
#
# if died:
#     print(f"Game over! ({start_row}, {start_col})")
#
# elif count <= 0:
#     print(f"You collected all coal! ({start_row}, {start_col})")
#
# if len(directions) == 0 and not died and count > 0:
#     print(f"{count} pieces of coal left. ({start_row}, {start_col})")

