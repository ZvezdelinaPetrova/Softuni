row, column = [int(x) for x in input().split()]

matrix = []

for r in range(row):
    matrix.append([] * column)
counter = 0
for row_index in range(row):
    for col_index in range(column):
        total_for_row = 97 + row_index
        first_and_last_letter = chr(total_for_row)
        total_for_col = 97 + col_index + counter
        middle_letter = chr(total_for_col)
        current_combo = first_and_last_letter + middle_letter + first_and_last_letter
        matrix[row_index].append(current_combo)
    counter += 1

for x in matrix:
    print(f"{' '.join(i for i in x)}")

# rows, columns = [int(x) for x in input().split(" ")]
#
# matrix = []
#
# for r in range(rows):
#     new_list = []
#     for c in range(columns):
#         main_str = chr(97 + r)
#         middle_str = chr(97 + r + c)
#         new_list.append(main_str + middle_str + main_str)
#
#     print(f"{' '.join([x for x in new_list])}")
