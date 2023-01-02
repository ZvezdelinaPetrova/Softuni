rows = int(input())

matrix = []

result = []

for r in range(rows):
    matrix.append([int(x) for x in input().split(", ")])

for l in matrix:
    for el in l:
        result.append(el)

print(result)

# row = int(input())
#
# matrix = []
#
# for r in range(row):
#     matrix.append([x for x in input().split(", ")])
#
# result = []
#
# for x in matrix:
#     for j in x:
#         result.append(int(j))
#
# print(result)