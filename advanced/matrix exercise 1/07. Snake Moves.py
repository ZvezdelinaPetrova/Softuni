from collections import deque

row, column = [int(x) for x in input().split()]
text = input()

word = deque(text)
for r in range(row):
    matrix = deque()
    if r % 2 == 0:
        for c in range(column):
            if word:
                letter = word.popleft()
                matrix.append(letter)
            else:
                word += text
                letter = word.popleft()
                matrix.append(letter)
        print(f"{''.join(x for x in matrix)}")
        word += text
    else:
        for c in range(column):
            if word:
                letter = word.popleft()
                matrix.append(letter)
            else:
                word += text
                letter = word.popleft()
                matrix.append(letter)
        print(f"{''.join(x for x in reversed(matrix))}")
        word += text

###############################################################
# from collections import deque
#
# row, column = [int(x) for x in input().split()]
# text = deque(input())
# matrix = []
#
# for r in range(row):
#     matrix.append(["x"] * column)
#
# for row in range(row):
#     for col in range(column):
#         current_char = text.popleft()
#         matrix[row][col] = current_char
#         text.append(current_char)
#
# for v in range(len(matrix)):
#     if v % 2 == 0:
#         print(''.join(matrix[v]))
#     else:
#         print(''.join(matrix[v][::-1]))
######################################################

# rows, columns = [int(x) for x in input().split(" ")]
# text = input()
# matrix = []
#
# for r in range(rows):
#     matrix.append(["x"] * columns)
#
# ind = 0
#
# for r in range(rows):
#     for c in range(columns):
#         matrix[r][c] = text[ind]
#         ind += 1
#         if ind == len(text):
#             ind = 0
#
# for r in range(rows):
#     if r % 2 == 0:
#         print(''.join(matrix[r]))
#     else:
#         print(''.join(matrix[r][::-1]))


