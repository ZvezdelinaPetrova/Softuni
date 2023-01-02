from collections import deque


def valid_index(r, c):
    return 0 <= r < size and 0 <= c < size


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


size = int(input())

matrix = []

number = int(input())

for _ in range(size):
    matrix.append(["-"] * size)

for x in range(number):
    command = input()
    o = command[1:-1]
    one, two = o.split(", ")
    index_1 = int(one)
    index_2 = int(two)
    matrix[index_1][index_2] = "*"

directions = deque(["left", "right", "up", "down", "d1", "d2", "d3", "d4"])

for row in range(size):
    for col in range(size):
        # el = matrix[row][col]
        if matrix[row][col] == '*':
            continue
        else:
            counter = 0
            for direction in directions:
                next_i_r, next_i_c = next_position(direction, row, col)
                if valid_index(next_i_r, next_i_c):
                    if matrix[next_i_r][next_i_c] == "*":
                        counter += 1
            matrix[row][col] = counter

for l in matrix:
    print(f"{' '.join(str(x) for x in l)}")
