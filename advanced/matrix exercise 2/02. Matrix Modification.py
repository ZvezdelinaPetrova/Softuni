def valid_index(one, two):
    if 0 <= one < row and 0 <= two < row:
        return True


row = int(input())

matrix = []

for _ in range(row):
    matrix.append([(int(x)) for x in input().split()])

command = input()

while command != "END":
    data = command.split()
    action = data[0]
    index_1, index_2 = int(data[1]), int(data[2])
    value = int(data[3])
    if not valid_index(index_1, index_2):
        print(f"Invalid coordinates")
    else:
        if action == "Add":
            matrix[index_1][index_2] += value
        elif action == "Subtract":
            matrix[index_1][index_2] -= value

    command = input()

for x in matrix:
    print(f"{' '.join(str(m) for m in x)}")

# def valid_index(needed_rows, needed_cols, needed_size):
#     return 0 <= needed_rows < needed_size and 0 <= needed_cols < needed_size
#
#
# rows = int(input())
#
# matrix = []
#
# for r in range(rows):
#     matrix.append([int(x) for x in input().split(" ")])
#
# command = input()
#
# while command != "END":
#     received_info = command.split()
#     command = received_info[0]
#     index_1 = int(received_info[1])
#     index_2 = int(received_info[2])
#     number = int(received_info[3])
#     # command = args[0]
#     # index_1, index_2, number = [int(x) for x in args[1:]]
#     if not valid_index(index_1, index_2, rows):
#         print("Invalid coordinates")
#     else:
#         if command == "Add":
#             matrix[index_1][index_2] += number
#         elif command == "Subtract":
#             matrix[index_1][index_2] -= number
#
#     command = input()
#
# for i in matrix:
#     print(f"{' '.join([str(x) for x in i])}")