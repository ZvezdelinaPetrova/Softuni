row = int(input())

matrix = []

for r in range(row):
    matrix.append([x for x in input()])

searched_thing = input()
position = ()
found = False
for x in range(row):
    for j in range(row):
        current_element = matrix[x][j]
        if current_element == searched_thing:
            position = (x, j)
            found = True
            break
    if found:
        break

if found:
    print(position)
else:
    print(f"{searched_thing} does not occur in the matrix")


# rows = int(input())
#
# matrix = []
#
# symbol_found = False
#
# for r in range(rows):
#     text = input()
#     matrix.append(list(text))
#
# symbol = input()
#
# for j in range(rows):
#     for c in range(rows):
#         current_element = matrix[j][c]
#         if current_element == symbol:
#             print(f"({j}, {c})")
#             symbol_found = True
#             break
#     if symbol_found:
#         break
# if not symbol_found:
#     print(f"{symbol} does not occur in the matrix")