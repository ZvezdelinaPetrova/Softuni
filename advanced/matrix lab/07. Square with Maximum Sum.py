row, column = [int(x) for x in input().split(", ")]

matrix = []

max_sum = float('-inf')

for r in range(row):
    matrix.append([int(x) for x in input().split(", ")])


def find_result_by_indexes(x, y):
    first = matrix[x][y]
    second = matrix[x + 1][y]
    third = matrix[x][y + 1]
    forth = matrix[x + 1][y + 1]
    sum_all = first + second + third + forth
    return sum_all


list_with_max_numbers = []

for x in range(row - 1):
    for y in range(column - 1):
        result = find_result_by_indexes(x, y)
        if result > max_sum:
            max_sum = result
            list_with_max_numbers.clear()
            list_with_max_numbers.append([matrix[x][y], matrix[x][y + 1]])
            list_with_max_numbers.append([matrix[x + 1][y], matrix[x + 1][y + 1]])

for k in list_with_max_numbers:
    print(f"{' '.join(str(x) for x in k)}")

print(max_sum)


# rows, columns = [int(x) for x in input().split(", ")]
#
# matrix = []
#
# max_sum = 0
# new_list = []
# second_list = []
# last_1 = 0
# last_2 = 0
# last_3 = 0
# last_4 = 0
#
# for r in range(rows):
#     matrix.append([int(x) for x in input().split(", ")])
#
# for r in range(rows - 1):
#     for col in range(columns - 1):
#         current_symbol = matrix[r][col]
#         next_symbol = matrix[r][col + 1]
#         third_symbol = matrix[r + 1][col]
#         forth_symbol = matrix[r + 1][col + 1]
#         current_sum = current_symbol + next_symbol + third_symbol + forth_symbol
#         if max_sum < current_sum:
#             max_sum = current_sum
#             last_1 = current_symbol
#             last_2 = next_symbol
#             last_3 = third_symbol
#             last_4 = forth_symbol
#
# new_list.append(last_1)
# new_list.append(last_2)
# second_list.append(last_3)
# second_list.append(last_4)
#
# print(*new_list)
# print(*second_list)
#
# print(max_sum)