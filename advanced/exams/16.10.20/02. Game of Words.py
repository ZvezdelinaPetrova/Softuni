from collections import deque


def valid_index(one, two):
    if 0 <= one < rows and 0 <= two < rows:
        return True


directions = {
    'right': lambda r, c: (r, c + 1),
    'left': lambda r, c: (r, c - 1),
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c)
}

word = deque(input())

rows = int(input())

p_row = 0
p_col = 0

matrix = []
for row in range(rows):
    row_elements = list(input())
    matrix.append(row_elements)
    for col in range(rows):
        el = row_elements[col]
        if el == 'P':
            p_row, p_col = row, col


commands = int(input())
for x in range(commands):
    command = input()
    next_row, next_col = directions[command](p_row, p_col)
    if valid_index(next_row, next_col):
        el = matrix[next_row][next_col]
        if el != "-":
            word.append(el)
        matrix[p_row][p_col] = "-"
        matrix[next_row][next_col] = "P"
        p_row, p_col = next_row, next_col
    else:
        if word:
            word.pop()


print(f"{''.join(x for x in word)}")
for l in matrix:
    print(f"{''.join(str(x) for x in l)}")