text = input()

new_string = ''
last_letter = ""

for i in text.lower():
    if i != last_letter:
        last_letter = i
        new_string += last_letter
print(new_string)
