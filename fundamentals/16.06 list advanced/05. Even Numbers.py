text = [int(el) for el in input().split(", ")]
new_list = []

# for el in range(len(text)):
#     new_number = text[el]
#     if new_number % 2 == 0:
#         index = el
#         new_list.append(index)
# print(new_list)

print([index for index in range(len(text)) if text[index] % 2 == 0])