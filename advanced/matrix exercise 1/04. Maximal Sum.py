row, column = [int(x) for x in input().split()]

matrix = []

max_sum = float('-inf')

for r in range(row):
    matrix.append([int(x) for x in input().split()])


def find_result_by_indexes(x, y):
    first = matrix[x][y]
    second = matrix[x + 1][y]
    third = matrix[x + 2][y]
    forth = matrix[x][y + 1]
    fifth = matrix[x + 1][y + 1]
    sixth = matrix[x + 2][y + 1]
    seventh = matrix[x][y + 2]
    eight = matrix[x + 1][y + 2]
    ninth = matrix[x + 2][y + 2]
    sum_all = first + second + third + forth + fifth + sixth + seventh + eight + ninth
    return sum_all


list_with_max_numbers = []

for x in range(row - 2):
    for y in range(column - 2):
        result = find_result_by_indexes(x, y)
        if result > max_sum:
            max_sum = result
            list_with_max_numbers.clear()
            list_with_max_numbers.append([matrix[x][y], matrix[x][y + 1], matrix[x][y + 2]])
            list_with_max_numbers.append([matrix[x + 1][y], matrix[x + 1][y + 1], matrix[x + 1][y + 2]])
            list_with_max_numbers.append([matrix[x + 2][y], matrix[x + 2][y + 1], matrix[x + 2][y + 2]])

print(f"Sum = {max_sum}")

for k in list_with_max_numbers:
    print(f"{' '.join(str(x) for x in k)}")


# rows, columns = [int(x) for x in input().split(" ")]
#
# matrix = []
#
# max_sum = 0
# first_list = []
# second_list = []
# third_list = []
# last_1 = 0
# last_2 = 0
# last_3 = 0
# last_4 = 0
# last_5 = 0
# last_6 = 0
# last_7 = 0
# last_8 = 0
# last_9 = 0
#
# for r in range(rows):
#     matrix.append([int(x) for x in input().split(" ")])
#
# for r in range(rows - 2):
#     for col in range(columns - 2):
#         first = matrix[r][col]
#         second = matrix[r][col + 1]
#         third = matrix[r][col + 2]
#         forth = matrix[r + 1][col]
#         fifth = matrix[r + 1][col + 1]
#         sixth = matrix[r + 1][col + 2]
#         seventh = matrix[r + 2][col]
#         eight = matrix[r + 2][col + 1]
#         ninth = matrix[r + 2][col + 2]
#         current_sum = first + second + third + forth + fifth + sixth + seventh + eight + ninth
#         if max_sum < current_sum:
#             max_sum = current_sum
#             last_1 = first
#             last_2 = second
#             last_3 = third
#             last_4 = forth
#             last_5 = fifth
#             last_6 = sixth
#             last_7 = seventh
#             last_8 = eight
#             last_9 = ninth
#
# first_list.append(last_1)
# first_list.append(last_2)
# first_list.append(last_3)
# second_list.append(last_4)
# second_list.append(last_5)
# second_list.append(last_6)
# third_list.append(last_7)
# third_list.append(last_8)
# third_list.append(last_9)
#
#
# print(f"Sum = {sum(first_list) + sum(second_list) + sum(third_list)}")
# print(*first_list)
# print(*second_list)
# print(*third_list)
#
# # if max_sum < current_sum:
# #     max_sum = current_sum
# #     best_row = r
# #     best_col = col
# #     gledame nachalnata poziciq na nai-dobrata matrica i posle v printa slagame pak koordinatite na drugite
# #     gore da ne zabravim da sazdaem best_row i best_col
# #     primeren print
# # print(matrix[best_row][best_col], matrix[best_row][best_col + 1], matrix[best_row][best_col + 2])
# # print(matrix[best_row + 1][best_col], matrix[best_row + 1][best_col + 1], matrix[best_row + 1][best_col + 2])
# # print(matrix[best_row + 2][best_col], matrix[best_row + 2][best_col + 1], matrix[best_row + 2][best_col + 2])