from collections import deque

row, column = [int(x) for x in input().split()]

matrix = []

for _ in range(row):
    matrix.append([x for x in input()])

commands = deque(x for x in input())


def valid_index(one, two):
    if 0 <= one < row and 0 <= two < column:
        return True


def next_position(direction, ro, col):
    if direction == "L":
        next_r, next_c = ro, col - 1
        return next_r, next_c
    if direction == "R":
        next_r, next_c = ro, col + 1
        return next_r, next_c
    if direction == "U":
        next_r, next_c = ro - 1, col
        return next_r, next_c
    if direction == "D":
        next_r, next_c = ro + 1, col
        return next_r, next_c


def bunny_spread(b_r, b_c):
    if valid_index(b_r, b_c - 1):
        matrix[b_r][b_c - 1] = "B"
    if valid_index(b_r, b_c + 1):
        matrix[b_r][b_c + 1] = "B"
    if valid_index(b_r - 1, b_c):
        matrix[b_r - 1][b_c] = "B"
    if valid_index(b_r + 1, b_c):
        matrix[b_r + 1][b_c] = "B"


died = False
win = False
player_row = ""
player_col = ""
last_row = ""
last_col = ""
bunnies = deque()
for r in range(row):
    for c in range(column):
        if matrix[r][c] == "P":
            player_row, player_col = r, c
        elif matrix[r][c] == "B":
            bunny_row, bunny_col = r, c
            bunnies.append(bunny_row)
            bunnies.append(bunny_col)
while True:
    if win:
        break
    if died:
        break
    current_command = commands.popleft()
    next_row, next_col = next_position(current_command, player_row, player_col)
    if not valid_index(next_row, next_col):
        win = True
        last_row, last_col = player_row, player_col
        matrix[last_row][last_col] = "."
    elif matrix[next_row][next_col] == ".":
        matrix[next_row][next_col] = "P"
        matrix[player_row][player_col] = "."
        player_row, player_col = next_row, next_col
    elif matrix[next_row][next_col] == "B":
        died = True
        player_row, player_col = next_row, next_col
    while bunnies:
        b_row = bunnies.popleft()
        b_col = bunnies.popleft()
        bunny_spread(b_row, b_col)
    if not win and matrix[player_row][player_col] == "B":
        died = True

    for rr in range(row):
        for cc in range(column):
            if matrix[rr][cc] == "B":
                bunny_row, bunny_col = rr, cc
                bunnies.append(bunny_row)
                bunnies.append(bunny_col)


for l in matrix:
    print(f"{''.join(x for x in l)}")


if died:
    print(f"dead: {player_row} {player_col}")
if win:
    print(f"won: {last_row} {last_col}")

#
# def is_inside(rows, cols, r, c):
#     return 0 <= r < rows and 0 <= c < cols
#
#
# def get_next_position(direction, row, col):
#     if direction == 'U':
#         return (row - 1, col)
#     if direction == 'D':
#         return (row + 1, col)
#     if direction == 'L':
#         return (row, col - 1)
#     return (row, col + 1)
#
#
# def get_next_bunnies(bunnies, rows, cols):
#     next_bunnies = []
#     for r, c in bunnies:
#         if is_inside(rows, cols, r - 1, c):
#             next_bunnies.append([r - 1, c])
#         if is_inside(rows, cols, r + 1, c):
#             next_bunnies.append([r + 1, c])
#         if is_inside(rows, cols, r, c - 1):
#             next_bunnies.append([r, c - 1])
#         if is_inside(rows, cols, r, c + 1):
#             next_bunnies.append([r, c + 1])
#     return next_bunnies
#
#
# rows, cols = [int(x) for x in input().split()]
#
# matrix = []
#
# player_row = 0
# player_col = 0
#
# bunnies = []
# for row in range(rows):
#     row_elements = list(input())
#     matrix.append(row_elements)
#     for col in range(cols):
#         el = row_elements[col]
#         if el == 'P':
#             player_row, player_col = row, col
#         elif el == 'B':
#             bunnies.append([row, col])
#
# commands = input()
#
# matrix[player_row][player_col] = '.'
#
# won = None
# for command in commands:
#     next_player_row, next_player_col = get_next_position(command, player_row, player_col)
#     if not is_inside(rows, cols, next_player_row, next_player_col):
#         won = True
#     elif matrix[next_player_row][next_player_col] == 'B':
#         won = False
#
#     if not won:
#         player_row, player_col = next_player_row, next_player_col
#
#     next_bunnies = get_next_bunnies(bunnies, rows, cols)
#     for r, c in next_bunnies:
#         if r == player_row and c == player_col and not won:
#             won = False
#         matrix[r][c] = 'B'
#     bunnies += next_bunnies
#     if won is not None:
#         break
#
# for row_elements in matrix:
#     print(''.join(row_elements))
#
# if won:
#     print(f'won: {player_row} {player_col}')
# else:
#     print(f'dead: {player_row} {player_col}')
