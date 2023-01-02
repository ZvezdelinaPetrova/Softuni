row = int(input())

matrix = []

total_primary = []
total_secondary = []

for r in range(row):
    matrix.append([(int(x)) for x in input().split()])

for row_index in range(row):
    total_primary.append(matrix[row_index][row_index])
    current_column = row - 1 - row_index
    total_secondary.append(matrix[row_index][current_column])


sum_all = abs(sum(total_primary) - sum(total_secondary))
print(sum_all)

# rows = int(input())
#
# matrix = []
# primary_diagonal = []
# secondary_diagonal = []
#
# for r in range(rows):
#     matrix.append([int(x) for x in input().split(" ")])
#
# for r in range(rows):
#     for c in range(rows):
#         current_element = matrix[r][c]
#         if r == c:
#             primary_diagonal.append(current_element)
#
# for i in range(rows):
#     current_el = matrix[i][rows - 1 - i]
#     secondary_diagonal.append(current_el)
#
# total = sum(primary_diagonal) - sum(secondary_diagonal)
#
# sum_all = abs(total)
#
# print(sum_all)
#
# # for r in range(rows):
# #    primary_diagonal.append(matrix[r][r])
# #    secondary_diagonal.append([r][rows - 1 - r])
