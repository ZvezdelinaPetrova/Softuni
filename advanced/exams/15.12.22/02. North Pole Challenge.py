def valid_index(r, c):
    return 0 <= r < rows and 0 <= c < cols


def if_all_found(dec, gif, cook):
    if dec == 0 and gif == 0 and cook == 0:
        return True


def check_new_indexes(r, c):
    if r < 0:
        r = rows - 1
    elif r >= rows:
        r = 0
    if c >= cols:
        c = 0
    elif c < 0:
        c = cols - 1
    return r, c


directions_move = {
    'right': lambda r, c: (r, c + 1),
    'left': lambda r, c: (r, c - 1),
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c)
}


rows, cols = [int(x) for x in input().split(", ")]
matrix = []

y_row = 0
y_col = 0

decorations = 0
gifts = 0
cookies = 0
d_found = 0
g_found = 0
c_found = 0
for row in range(rows):
    row_elements = list(input().split())
    matrix.append(row_elements)
    for col in range(cols):
        el = row_elements[col]
        if el == 'Y':
            y_row, y_col = row, col
        elif el == "D":
            decorations += 1
        elif el == "G":
            gifts += 1
        elif el == "C":
            cookies += 1

command = input()
founded = False
while command != "End":
    command = command.split("-")
    direction = command[0]
    steps = int(command[1])
    while steps > 0:
        matrix[y_row][y_col] = "x"
        next_p1, next_p2 = directions_move[direction](y_row, y_col)
        if valid_index(next_p1, next_p2):
            if matrix[next_p1][next_p2] == "D":
                decorations -= 1
                d_found += 1
            elif matrix[next_p1][next_p2] == "G":
                gifts -= 1
                g_found += 1
            elif matrix[next_p1][next_p2] == "C":
                cookies -= 1
                c_found += 1
            if if_all_found(decorations, gifts, cookies):
                print(f"Merry Christmas!")
                founded = True
                matrix[next_p1][next_p2] = "Y"
                break
            y_row, y_col = next_p1, next_p2

        else:
            next_p1, next_p2 = check_new_indexes(next_p1, next_p2)
            if matrix[next_p1][next_p2] == "D":
                decorations -= 1
                d_found += 1
            elif matrix[next_p1][next_p2] == "G":
                gifts -= 1
                g_found += 1
            elif matrix[next_p1][next_p2] == "C":
                cookies -= 1
                c_found += 1
            if if_all_found(decorations, gifts, cookies):
                print(f"Merry Christmas!")
                founded = True
                matrix[next_p1][next_p2] = "Y"
                break
            y_row, y_col = next_p1, next_p2
        steps -= 1
    if founded:
        break
    matrix[y_row][y_col] = "Y"
    command = input()


print(f"You've collected:")
print(f"- {d_found} Christmas decorations")
print(f"- {g_found} Gifts")
print(f"- {c_found} Cookies")

for l in matrix:
    print(f"{' '.join(str(x) for x in l)}")

