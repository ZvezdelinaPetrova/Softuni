def valid_index(r, c):
    return 0 <= r < size and 0 <= c < size


directions = {
    'right': lambda r, c: (r, c + steps),
    'left': lambda r, c: (r, c - steps),
    'up': lambda r, c: (r - steps, c),
    'down': lambda r, c: (r + steps, c)
}

directions_shoot = {
    'right': lambda r, c: (r, c + 1),
    'left': lambda r, c: (r, c - 1),
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c)
}

size = 5

matrix = []

a_row = 0
a_col = 0
targets = 0
hit = 0
gg = False
indexes = []
for row in range(size):
    row_elements = list(input().split())
    matrix.append(row_elements)
    for col in range(size):
        el = row_elements[col]
        if el == 'A':
            a_row, a_col = row, col
        elif el == "x":
            targets += 1

commands = int(input())

for x in range(commands):
    if gg:
        break
    d = input().split()
    action = d[0]
    direction = d[1]
    if action == "shoot":
        next_row, next_col = directions_shoot[direction](a_row, a_col)
        while True:
            if valid_index(next_row, next_col):
                if matrix[next_row][next_col] == "x":
                    hit += 1
                    targets -= 1
                    matrix[next_row][next_col] = "."
                    indexes.append([next_row, next_col])
                    if targets == 0:
                        print(f"Training completed! All {hit} targets hit.")
                        gg = True
                    break
                next_row, next_col = directions_shoot[direction](next_row, next_col)
            else:
                break
    elif action == "move":
        steps = int(d[2])
        next_row, next_col = directions[direction](a_row, a_col)
        if not valid_index(next_row, next_col):
            continue
        if matrix[next_row][next_col] == ".":
            matrix[next_row][next_col] = "A"
            a_row, a_col = next_row, next_col

if not gg:
    print(f"Training not completed! {targets} targets left.")

for l in indexes:
    print(l)


# def valid_index(r, c, rows):
#     return 0 <= r < rows and 0 <= c < rows
#
#
# def move_to_next_position(rol, col, direction, steps):
#     if direction == "up":
#         return rol - steps, col
#     if direction == "down":
#         return rol + steps, col
#     if direction == "right":
#         return rol, col + steps
#     if direction == "left":
#         return rol, col - steps
#
#
# rows = 5
#
# matrix = []
#
# player_row = 0
# player_col = 0
# targets = 0
# hit_targets = 0
#
# for row in range(rows):
#     row_elements = list(input().split())
#     matrix.append(row_elements)
#     for col in range(rows):
#         el = row_elements[col]
#         if el == 'A':
#             player_row, player_col = row, col
#         elif el == "x":
#             targets += 1
#
# initial_targets = targets
#
# number_of_commands = int(input())
# shot_indexes = []
# completed = False
#
# for x in range(number_of_commands):
#     command = input().split()
#     action = command[0]
#     direction = command[1]
#     current_row, current_col = player_row, player_col
#     if action == "move":
#         steps_to_move = int(command[2])
#
#         index_1, index_2 = move_to_next_position(current_row, current_col, direction, steps_to_move)
#         if valid_index(index_1, index_2, rows):
#             if matrix[index_1][index_2] == ".":
#                 matrix[index_1][index_2] = "A"
#                 matrix[player_row][player_col] = "."
#                 player_row, player_col = index_1, index_2
#     elif action == "shoot":
#
#         while True:
#             index_1, index_2 = move_to_next_position(current_row, current_col, direction, 1)
#             if valid_index(index_1, index_2, rows):
#                 if matrix[index_1][index_2] == "x":
#                     targets -= 1
#                     hit_targets += 1
#                     shot_indexes.append([index_1, index_2])
#                     matrix[index_1][index_2] = "."
#                     if targets <= 0:
#                         completed = True
#                         break
#                     break
#             else:
#                 break
#
#             current_row, current_col = index_1, index_2
#     if completed:
#         break
#
# if not completed:
#     print(f"Training not completed! {initial_targets - hit_targets} targets left.")
# else:
#     print(f"Training completed! All {initial_targets} targets hit.")
#
# for x in range(len(shot_indexes)):
#     print(shot_indexes[x])