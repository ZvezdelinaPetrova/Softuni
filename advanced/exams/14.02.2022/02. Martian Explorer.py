from collections import deque


def valid_index(r, c):
    return 0 <= r < size and 0 <= c < size


directions = {
    'right': lambda r, c: (r, c + 1),
    'left': lambda r, c: (r, c - 1),
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c)
}

size = 6

matrix = []

m_row = 0
m_col = 0


for row in range(size):
    row_elements = list(input().split())
    matrix.append(row_elements)
    for col in range(size):
        el = row_elements[col]
        if el == 'E':
            m_row, m_col = row, col

collected = []
directions_list = deque(x for x in input().split(", "))
broken = False
while directions_list:
    current_direction = directions_list.popleft()
    next_row, next_col = directions[current_direction](m_row, m_col)
    if valid_index(next_row, next_col):
        if matrix[next_row][next_col] == "W":
            collected.append("W")
            print(f"Water deposit found at ({next_row}, {next_col})")
        elif matrix[next_row][next_col] == "M":
            collected.append("M")
            print(f"Metal deposit found at ({next_row}, {next_col})")
        elif matrix[next_row][next_col] == "C":
            collected.append("C")
            print(f"Concrete deposit found at ({next_row}, {next_col})")
        elif matrix[next_row][next_col] == "R":
            broken = True
            print(f"Rover got broken at ({next_row}, {next_col})")
            break
    else:
        if next_row < 0:
            next_row = 5
        elif next_row > 5:
            next_row = 0
        if next_col > 5:
            next_col = 0
        elif next_col < 0:
            next_col = 5

        if matrix[next_row][next_col] == "W":
            collected.append("W")
            print(f"Water deposit found at ({next_row}, {next_col})")
        elif matrix[next_row][next_col] == "M":
            collected.append("M")
            print(f"Metal deposit found at ({next_row}, {next_col})")
        elif matrix[next_row][next_col] == "C":
            collected.append("C")
            print(f"Concrete deposit found at ({next_row}, {next_col})")
        elif matrix[next_row][next_col] == "R":
            broken = True
            print(f"Rover got broken at ({next_row}, {next_col})")
            break

    m_row, m_col = next_row, next_col


if ("M" in collected) and ("W" in collected) and ("C" in collected):
    print("Area suitable to start the colony.")
else:
    print(f"Area not suitable to start the colony.")
