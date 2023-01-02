from collections import deque


def valid_index(one, two):
    if 0 <= one < size and 0 <= two < size:
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
    if direction == "d1":
        next_r, next_c = ro - 1, col - 1
        return next_r, next_c
    if direction == "d2":
        next_r, next_c = ro - 1, col + 1
        return next_r, next_c
    if direction == "d3":
        next_r, next_c = ro + 1, col - 1
        return next_r, next_c
    if direction == "d4":
        next_r, next_c = ro + 1, col + 1
        return next_r, next_c


size = 8
k_row = 0
k_col = 0
matrix = []
queens = deque()
for _ in range(size):
    matrix.append(input().split())

for row in range(size):
    for col in range(size):
        el = matrix[row][col]
        if el == 'K':
            k_row, k_col = row, col

directions = deque(["left", "right", "up", "down", "d1", "d2", "d3", "d4"])
while directions:
    ind_1, ind_2 = k_row, k_col
    d = directions.popleft()
    next_i_r, next_i_c = next_position(d, ind_1, ind_2)
    while valid_index(next_i_r, next_i_c):
        if valid_index(next_i_r, next_i_c):
            if matrix[next_i_r][next_i_c] == "Q":
                queens.append([next_i_r, next_i_c])
                break
            next_i_r, next_i_c = next_position(d, next_i_r, next_i_c)

if not queens:
    print(f"The king is safe!")
else:
    for x in queens:
        print(x)

# def is_in_range(row, col, n):
#     if 0 <= row < n and 0 <= col < n:
#         return True
#     return False
#
#
# matrix = []
# n = 8
# for _ in range(n):
#     matrix.append(input().split())
#
# directions = {
#     'up':(-1, 0),
#     'down':(1, 0),
#     'left':(0, -1),
#     'right':(0, 1),
#     'up_right':(-1, 1),
#     'up_left':(-1, -1),
#     'down_right':(1, 1),
#     'down_left':(1, -1),
# }
# queens = []
# for row in range(n):
#     for col in range(n):
#         if matrix[row][col] == 'Q':
#             for direction in directions:
#                 next_row = row + directions[direction][0]
#                 next_col = col + directions[direction][1]
#                 while is_in_range(next_row, next_col, n):
#                     if matrix[next_row][next_col] == 'Q':
#                         break
#                     if matrix[next_row][next_col] == 'K':
#                         queens.append([row, col])
#                         break
#                     next_row += directions[direction][0]
#                     next_col += directions[direction][1]
#
# if queens:
#     [print(pos) for pos in queens]
# else:
#     print('The king is safe!')


