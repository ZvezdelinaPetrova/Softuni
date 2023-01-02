row, column = [int(x) for x in input().split()]

matrix = []


for r in range(row):
    matrix.append([x for x in input().split()])


def find_elements_by_indexes(x, y):
    first = matrix[x][y]
    second = matrix[x + 1][y]
    third = matrix[x][y + 1]
    forth = matrix[x + 1][y + 1]
    if first == second == third == forth:
        return True
    return False


counter = 0
for x in range(row - 1):
    for y in range(column - 1):
        result = find_elements_by_indexes(x, y)
        if result:
            counter += 1

print(counter)


# rows, columns = [int(x) for x in input().split(" ")]
#
# matrix = []
#
# count = 0
#
# for r in range(rows):
#     matrix.append([x for x in input().split(" ")])
#
# for r in range(rows - 1):
#     for col in range(columns - 1):
#         current_symbol = matrix[r][col]
#         second_symbol = matrix[r][col + 1]
#         third_symbol = matrix[r + 1][col]
#         forth_symbol = matrix[r + 1][col + 1]
#         if current_symbol == second_symbol == third_symbol == forth_symbol:
#             count += 1
# print(count)