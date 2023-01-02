text = input()
new_string = ''
strength = 0
i = 0
while i < len(text):
    current_symbol = text[i]
    if current_symbol == ">":
        new_string += current_symbol
        strength += int(text[i + 1])
    else:
        if strength > 0:
            strength -= 1
        else:
            new_string += current_symbol
    i += 1

print(new_string)