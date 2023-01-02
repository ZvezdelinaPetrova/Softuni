def valid_index(r, c, rows):
    return 0 <= r < rows and 0 <= c < rows


rows = int(input())

matrix = []

b_row = 0
b_col = 0

for row in range(rows):
    row_elements = list(input().split())
    matrix.append(row_elements)
    for col in range(rows):
        el = row_elements[col]
        if el == 'B':
            b_row, b_col = row, col

max_number = float('-inf')
best_direction = ''
best_indexes = []

directions = {
    'right': lambda r, c: (r, c + 1),
    'left': lambda r, c: (r, c - 1),
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c)
}

for direction, step in directions.items():
    count = 0
    current_row, current_col = b_row, b_col
    indexes = []

    while True:
        current_row, current_col = step(current_row, current_col)
        if not valid_index(current_row, current_col, rows):
            break
        if matrix[current_row][current_col] == 'X':
            break
        count += int(matrix[current_row][current_col])
        indexes.append([current_row, current_col])

    if count >= max_number and indexes:
        max_number, best_direction, best_indexes = count, direction, indexes

print(best_direction)

for step in best_indexes:
    print(step)
print(max_number)

# from collections import deque
#
#
# def valid_index(r, c):
#     if 0 <= r < size and 0 <= c < size:
#         return True
#
#
# def find_sum(direction, row, col):
#     current_sum = 0
#     while True:
#         if direction == "up":
#             row -= 1
#             if valid_index(row, col):
#                 if matrix[row][col] == "X":
#                     break
#                 current_sum += int(matrix[row][col])
#                 path.append([row, col])
#             else:
#                 break
#         elif direction == "down":
#             row += 1
#             if valid_index(row, col):
#                 if matrix[row][col] == "X":
#                     break
#                 current_sum += int(matrix[row][col])
#                 path.append([row, col])
#             else:
#                 break
#         elif direction == "left":
#             col -= 1
#             if valid_index(row, col):
#                 if matrix[row][col] == "X":
#                     break
#                 current_sum += int(matrix[row][col])
#                 path.append([row, col])
#             else:
#                 break
#         elif direction == "right":
#             col += 1
#             if valid_index(row, col):
#                 if matrix[row][col] == "X":
#                     break
#                 current_sum += int(matrix[row][col])
#                 path.append([row, col])
#             else:
#                 break
#     return current_sum
#
#
# size = int(input())
#
# matrix = []
#
# for _ in range(size):
#     matrix.append([x for x in input().split()])
#
# b_row = ""
# b_col = ""
# max_sum = float('-inf')
#
# for r in range(size):
#     for c in range(size):
#         if matrix[r][c] == "B":
#             b_row, b_col = r, c
#
# directions = deque(["up", "down", "left", "right"])
#
# best_direction = ''
# best_path = []
# while directions:
#     path = []
#     current_direction = directions.popleft()
#     result = find_sum(current_direction, b_row, b_col)
#     if result > max_sum and path:
#         max_sum = result
#         best_path = path
#         best_direction = current_direction
#
# print(best_direction)
#
#
# for x in best_path:
#     print(x)
#
# print(max_sum)
