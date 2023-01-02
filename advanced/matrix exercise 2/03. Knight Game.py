def valid_index(one, two):
    if 0 <= one < size and 0 <= two < size:
        return True


def find_kills(current_kills, r, col):
    if valid_index(r - 2, col - 1) and matrix[r - 2][col - 1] == "K":
        current_kills += 1
    if valid_index(r - 2, col + 1) and matrix[r - 2][col + 1] == "K":
        current_kills += 1
    if valid_index(r + 2, col - 1) and matrix[r + 2][col - 1] == "K":
        current_kills += 1
    if valid_index(r + 2, col + 1) and matrix[r + 2][col + 1] == "K":
        current_kills += 1
    if valid_index(r - 1, col - 2) and matrix[r - 1][col - 2] == "K":
        current_kills += 1
    if valid_index(r - 1, col + 2) and matrix[r - 1][col + 2] == "K":
        current_kills += 1
    if valid_index(r + 1, col - 2) and matrix[r + 1][col - 2] == "K":
        current_kills += 1
    if valid_index(r + 1, col + 2) and matrix[r + 1][col + 2] == "K":
        current_kills += 1
    return current_kills


size = int(input())

matrix = []

for _ in range(size):
    matrix.append([x for x in input()])

max_kills = 0
coordinates = []
removed = 0

while True:
    max_kills = 0
    for row in range(size):
        for column in range(size):
            if matrix[row][column] == "K":
                current_kills = 0
                current_row, current_col = row, column
                result = find_kills(current_kills, current_row, current_col)
                if result > max_kills:
                    max_kills = result
                    coordinates.clear()
                    coordinates.append(current_row)
                    coordinates.append(current_col)
                    #             if count > max_count:
                    #                 max_count, knight_row, knight_col = count, r, c
                    #     if max_count == 0:
                    #         break
                    #     else:
                    #         matrix[knight_row][knight_col] = '0'
                    #         knights += 1
    if max_kills == 0:
        break
    elif coordinates:
        first = coordinates[0]
        second = coordinates[1]
        matrix[first][second] = "0"
        coordinates.clear()
        removed += 1

print(removed)

# def valid_index(needed_rows, needed_cols, needed_size):
#     return 0 <= needed_rows < needed_size and 0 <= needed_cols < needed_size
#
#
# def how_many_kills(needed_rows, needed_cols, size, current_matrix):
#     result = 0
#
#     if valid_index(needed_rows - 2, needed_cols - 1, rows) and matrix[needed_rows - 2][needed_cols - 1] == "K":
#         result += 1
#     if valid_index(needed_rows - 2, needed_cols + 1, rows) and matrix[needed_rows - 2][needed_cols + 1] == "K":
#         result += 1
#     if valid_index(needed_rows + 2, needed_cols - 1, rows) and matrix[needed_rows + 2][needed_cols - 1] == "K":
#         result += 1
#     if valid_index(needed_rows + 2, needed_cols + 1, rows) and matrix[needed_rows + 2][needed_cols + 1] == "K":
#         result += 1
#     if valid_index(needed_rows - 1, needed_cols - 2, rows) and matrix[needed_rows - 1][needed_cols - 2] == "K":
#         result += 1
#     if valid_index(needed_rows - 1, needed_cols + 2, rows) and matrix[needed_rows - 1][needed_cols + 2] == "K":
#         result += 1
#     if valid_index(needed_rows + 1, needed_cols - 2, rows) and matrix[needed_rows + 1][needed_cols - 2] == "K":
#         result += 1
#     if valid_index(needed_rows + 1, needed_cols + 2, rows) and matrix[needed_rows + 1][needed_cols + 2] == "K":
#         result += 1
#
#     return result
#
#
# rows = int(input())
#
# matrix = []
#
# for _ in range(rows):
#     matrix.append([x for x in input()])
#
#
# knights = 0
#
# while True:
#     max_count, knight_row, knight_col = 0, 0, 0
#     for r in range(rows):
#         for c in range(rows):
#             if matrix[r][c] == '0':
#                 continue
#             count = how_many_kills(r, c, rows, matrix)
#             if count > max_count:
#                 max_count, knight_row, knight_col = count, r, c
#     if max_count == 0:
#         break
#     else:
#         matrix[knight_row][knight_col] = '0'
#         knights += 1
#
# print(knights)

