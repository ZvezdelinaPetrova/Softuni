data = input()

new_list = []
reversed_list = []

for ch in data:
    new_list.append(ch)

while new_list:
    reversed_letter = new_list.pop()
    reversed_list.append(reversed_letter)
print("".join(reversed_list))


# text = input()
# new_text = [x for x in text]
# final = ''
#
# while new_text:
#     ch = new_text.pop()
#     final += ch
#
# print(final)