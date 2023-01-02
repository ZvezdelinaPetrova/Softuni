text = input()

new_list = []

for j in text:
    letter_as_number = ord(j) + 3
    new_letter = chr(letter_as_number)
    new_list.append(new_letter)

print("".join(new_list))