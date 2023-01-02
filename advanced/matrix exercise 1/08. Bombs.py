row = int(input())

matrix = []

for r in range(row):
    matrix.append([int(x) for x in input().split()])

given_indexes = [x for x in input().split()]


def valid_index(one, two):
    if 0 <= one < row and 0 <= two < row:
        return True


def reduce_other_cells(index_1, index_2, dmg):
    if valid_index(index_1 - 1, index_2):
        if matrix[index_1 - 1][index_2] > 0:
            matrix[index_1 - 1][index_2] -= dmg
    if valid_index(index_1 + 1, index_2):
        if matrix[index_1 + 1][index_2] > 0:
            matrix[index_1 + 1][index_2] -= dmg
    if valid_index(index_1, index_2 - 1):
        if matrix[index_1][index_2 - 1] > 0:
            matrix[index_1][index_2 - 1] -= dmg
    if valid_index(index_1, index_2 + 1):
        if matrix[index_1][index_2 + 1] > 0:
            matrix[index_1][index_2 + 1] -= dmg
    if valid_index(index_1 - 1, index_2 - 1):
        if matrix[index_1 - 1][index_2 - 1] > 0:
            matrix[index_1 - 1][index_2 - 1] -= dmg
    if valid_index(index_1 - 1, index_2 + 1):
        if matrix[index_1 - 1][index_2 + 1] > 0:
            matrix[index_1 - 1][index_2 + 1] -= dmg
    if valid_index(index_1 + 1, index_2 - 1):
        if matrix[index_1 + 1][index_2 - 1] > 0:
            matrix[index_1 + 1][index_2 - 1] -= dmg
    if valid_index(index_1 + 1, index_2 + 1):
        if matrix[index_1 + 1][index_2 + 1] > 0:
            matrix[index_1 + 1][index_2 + 1] -= dmg


for x in given_indexes:
    index_one, index_two = x.split(",")
    index_1 = int(index_one)
    index_2 = int(index_two)
    damage = matrix[index_1][index_2]
    if matrix[index_1][index_2] <= 0:
        continue
    matrix[index_1][index_2] = 0
    reduce_other_cells(index_1, index_2, damage)

alive = []
for k in matrix:
    for g in k:
        if g > 0:
            alive.append(g)

print(f"Alive cells: {len(alive)}")
print(f"Sum: {sum(alive)}")

for l in matrix:
    print(f"{' '.join(str(x) for x in l)}")


# def is_valid_index(rol, col, row):
#     if rol < 0 or col < 0 or rol >= row or col >= row:
#         return False
#     return True
#
#
# rows = int(input())
#
# matrix = []
#
# for _ in range(rows):
#     matrix.append([int(x) for x in input().split()])
#
# indexes = input().split()
#
# for i in indexes:
#     index_1, index_2 = i.split(",")
#     r = int(index_1)
#     c = int(index_2)
#     current_element = int(matrix[r][c])
#     if current_element <= 0:
#         continue
#     matrix[r][c] = 0
#     if is_valid_index(r - 1, c - 1, rows) and matrix[r - 1][c - 1] > 0:
#         matrix[r - 1][c - 1] -= current_element
#     if is_valid_index(r - 1, c, rows) and matrix[r - 1][c] > 0:
#         matrix[r - 1][c] -= current_element
#     if is_valid_index(r - 1, c + 1, rows) and matrix[r - 1][c + 1] > 0:
#         matrix[r - 1][c + 1] -= current_element
#     if is_valid_index(r, c - 1, rows) and matrix[r][c - 1] > 0:
#         matrix[r][c - 1] -= current_element
#     if is_valid_index(r, c + 1, rows) and matrix[r][c + 1] > 0:
#         matrix[r][c + 1] -= current_element
#     if is_valid_index(r + 1, c, rows) and matrix[r + 1][c] > 0:
#         matrix[r + 1][c] -= current_element
#     if is_valid_index(r + 1, c + 1, rows) and matrix[r + 1][c + 1] > 0:
#         matrix[r + 1][c + 1] -= current_element
#     if is_valid_index(r + 1, c - 1, rows) and matrix[r + 1][c - 1] > 0:
#         matrix[r + 1][c - 1] -= current_element
#
# total = 0
# alive = 0
#
# for el in matrix:
#     for i in el:
#         if i > 0:
#             total += i
#             alive += 1
#
# print(f"Alive cells: {alive}")
# print(f"Sum: {total}")
#
# for i in matrix:
#     print(' '.join([str(x) for x in i]))