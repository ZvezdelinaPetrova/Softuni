rows, columns = [int(x) for x in input().split(", ")]

matrix = []
result = 0

for r in range(rows):
    matrix.append([int(x) for x in input().split(", ")])
    result += sum(matrix[r])

print(result)
print(matrix)


# row, column = input().split(", ")
# row, column = int(row), int(column)
#
# matrix = []
# sum_all = 0
# for r in range(row):
#     text = input().split(",")
#     current_row = [int(x) for x in text]
#     matrix.append(current_row)
#
#
# for j in matrix:
#     sum_all += sum(j)
# print(sum_all)
# print(matrix)