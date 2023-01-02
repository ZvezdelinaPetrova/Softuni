from collections import deque


def valid_index(r, c):
    return 0 <= r < size and 0 <= c < size


def check_if_w_kill(row, col):
    if valid_index(row, col - 1):
        if matrix[row][col - 1] == "b" or matrix[row][col - 1] == "w":
            return row, col - 1
    if valid_index(row, col + 1):
        if matrix[row][col + 1] == "b" or matrix[row][col + 1] == "w":
            return row, col + 1


def next_direction(r, c):
    n_r = ""
    n_c = ""
    if current_player == "w":
        n_r, n_c = r - 1, c
    elif current_player == "b":
        n_r, n_c = r + 1, c
    return n_r, n_c


size = 8
matrix = []

w_row = ""
w_col = ""
b_row = ""
b_col = ""


for row in range(size):
    row_elements = list(input().split())
    matrix.append(row_elements)
    for col in range(size):
        el = row_elements[col]
        if el == 'w':
            w_row, w_col = row, col
        elif el == "b":
            b_row, b_col = row, col
players = deque(["w", "b"])
while True:
    current_player = players.popleft()
    if current_player == "w":
        next_row, next_col = next_direction(w_row, w_col)
        if next_row == 0:
            print(f"Game over! White pawn is promoted to a queen at {f'{chr(97 + next_col)}{chr(56 - next_row)}'}.")
            break
        if check_if_w_kill(next_row, next_col):
            kill_r, kill_c = check_if_w_kill(next_row, next_col)
            print(f"Game over! White win, capture on {f'{chr(97 + kill_c)}{chr(56 - kill_r)}'}.")
            break
        w_row, w_col = next_row, next_col
        matrix[w_row][w_col] = "w"
    elif current_player == "b":
        next_row, next_col = next_direction(b_row, b_col)
        if next_row == 7:
            print(f"Game over! Black pawn is promoted to a queen at {f'{chr(97 + next_col)}{chr(56 - next_row)}'}.")
            break
        if check_if_w_kill(next_row, next_col):
            kill_r, kill_c = check_if_w_kill(next_row, next_col)
            print(f"Game over! Black win, capture on {f'{chr(97 + kill_c)}{chr(56 - kill_r)}'}.")
            break
        b_row, b_col = next_row, next_col
        matrix[b_row][b_col] = "b"

    players.append(current_player)