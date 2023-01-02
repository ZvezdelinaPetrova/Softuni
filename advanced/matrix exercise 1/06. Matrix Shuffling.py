row, column = [int(x) for x in input().split()]

matrix = []


def valid_indexes(index_1, index_2, index_3, index_4):
    if (0 <= index_1 < row) and (0 <= index_3 < row) and (0 <= index_2 < column) and (0 <= index_4 < column):
        return True


for r in range(row):
    matrix.append([x for x in input().split()])

command = input()
while command != "END":
    text = command.split()
    if text[0] != "swap" or len(text) > 5:
        print(f"Invalid input!")
    else:
        i_one = int(text[1])
        i_two = int(text[2])
        i_three = int(text[3])
        i_four = int(text[4])
        if valid_indexes(i_one, i_two, i_three, i_four):
            matrix[i_one][i_two], matrix[i_three][i_four] = matrix[i_three][i_four], matrix[i_one][i_two]
            for el in matrix:
                print(f"{' '.join(str(x) for x in el)}")
        else:
            print(f"Invalid input!")
    command = input()

# rows, columns = [int(x) for x in input().split(" ")]
#
# matrix = []
#
# for r in range(rows):
#     matrix.append([x for x in input().split(" ")])
#
# command = input()
#
# while command != "END":
#     received_info = command.split()
#     if command[0] != "swap" and len(received_info) != 5:
#         print("Invalid input!")
#     else:
#         el_1 = int(received_info[1])
#         el_2 = int(received_info[2])
#         el_3 = int(received_info[3])
#         el_4 = int(received_info[4])
#
#         if 0 <= el_1 < rows and 0 <= el_2 < columns \
#                 and 0 <= el_3 < rows and 0 <= el_4 < columns:
#             first_element = matrix[el_1][el_2]
#             second_element = matrix[el_3][el_4]
#             matrix[el_3][el_4], matrix[el_1][el_2] = first_element, second_element
#             for i in matrix:
#                 print(f"{' '.join([str(x) for x in i])}")
#         else:
#             print("Invalid input!")
#
#     command = input()