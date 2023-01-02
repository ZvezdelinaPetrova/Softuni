row = int(input())

matrix = []

total = 0

for r in range(row):
    matrix.append([(int(x)) for x in input().split()])

for row_index in range(row):
    column = row_index
    total += matrix[row_index][column]
    column += row_index + 1

print(total)


# rows = int(input())
#
# matrix = []
#
# results = 0
#
# for r in range(rows):
#     matrix.append([int(x) for x in input().split(" ")])
#
# for j in range(rows):
#     for c in range(rows):
#         current_element = matrix[j][c]
#         if j == c:
#             results += current_element
#
# print(results)