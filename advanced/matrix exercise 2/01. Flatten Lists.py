data = input().split("|")

matrix = []

for el in data:
    result = el.strip()
    matrix.append(result.split())

final = [x for x in reversed(matrix)]
for l in final:
    for el in l:
        print(el, end=" ")

# text = input().split("|")
#
# new_list = []
#
# for i in range(len(text) - 1, -1, -1):
#     for el in text[i].split():
#         new_list.append(el)
#
# print(*new_list)