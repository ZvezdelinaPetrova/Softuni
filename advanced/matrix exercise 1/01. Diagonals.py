row = int(input())

matrix = []

total_primary = []
total_secondary = []

for r in range(row):
    matrix.append([(int(x)) for x in input().split(", ")])

for row_index in range(row):
    total_primary.append(matrix[row_index][row_index])
    current_column = row - 1 - row_index
    total_secondary.append(matrix[row_index][current_column])


print(f"Primary diagonal: {', '.join(str(x) for x in total_primary)}. Sum: {sum(total_primary)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in total_secondary)}. Sum: {sum(total_secondary)}")


# rows = int(input())
#
# matrix = []
# primary_diagonal = []
# secondary_diagonal = []
#
# for r in range(rows):
#     matrix.append([int(x) for x in input().split(", ")])
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
# list_1 = (str(x) for x in primary_diagonal)
# list_2 = (str(x) for x in secondary_diagonal)
#
# print(f"Primary diagonal: {', '.join(list_1)}. Sum: {sum(primary_diagonal)}")
# print(f"Secondary diagonal: {', '.join(list_2)}. Sum: {sum(secondary_diagonal)}")
# # print(f"Primary diagonal: {', '.join([str(x) for x in primary_diagonal])}. Sum: {sum(primary_diagonal)}")