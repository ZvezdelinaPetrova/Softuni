from math import floor
from collections import deque


def valid_index(r, c):
    return 0 <= r < size and 0 <= c < size


directions = {
    'right': lambda r, c: (r, c + 1),
    'left': lambda r, c: (r, c - 1),
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c)
}


def check_new_indexes(r, c):
    if r < 0:
        r = size - 1
    elif r >= size:
        r = 0
    if c >= size:
        c = 0
    elif c < 0:
        c = size - 1
    return r, c


size = int(input())

matrix = []

p_row = 0
p_col = 0
coins = 0
positions = []
lose = False

for row in range(size):
    row_elements = list(input().split())
    matrix.append(row_elements)
    for col in range(size):
        el = row_elements[col]
        if el == 'P':
            p_row, p_col = row, col
matrix[p_row][p_col] = "-"
positions.append([p_row, p_col])

text = input()
while text:
    command = text
    if command != "up" and command != "down" and command != "left" and command != "right":
        continue
    next_row, next_col = directions[command](p_row, p_col)
    if valid_index(next_row, next_col):
        positions.append([next_row, next_col])
        el = matrix[next_row][next_col]
        if el == "X":
            coins = floor(coins / 2)
            lose = True
            break
        elif el == "-":
            p_row, p_col = next_row, next_col
        else:
            coins += int(el)

    else:
        next_row, next_col = check_new_indexes(next_row, next_col)
        positions.append([next_row, next_col])
        el = matrix[next_row][next_col]
        if el == "X":
            coins = floor(coins / 2)
            lose = True
            break
        elif el == "-":
            p_row, p_col = next_row, next_col
        else:
            coins += int(el)
    if coins >= 100:
        break
    matrix[next_row][next_col] = "-"
    p_row, p_col = next_row, next_col
    text = input()


if not lose and coins >= 100:
    print(f"You won! You've collected {coins} coins.")
else:
    print(f"Game over! You've collected {coins} coins.")

print(f"Your path:")
for x in positions:
    print(x)
