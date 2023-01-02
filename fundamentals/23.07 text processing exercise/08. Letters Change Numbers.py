text = input()
text = str.split(text)

new_list = []

result = 0
for word in text:
    result = 0
    first_letter = word[0]
    last_letter = word[-1]
    middle_number = int(word[1:-1])
    if first_letter.isupper():
        number_of_first_letter = ord(first_letter) - 64
        result = middle_number / number_of_first_letter
    elif first_letter.islower():
        number_of_first_letter = ord(first_letter) - 96
        result = middle_number * number_of_first_letter
    if last_letter.isupper():
        number_of_last_letter = ord(last_letter) - 64
        result -= number_of_last_letter
    elif last_letter.islower():
        number_of_last_letter = ord(last_letter) - 96
        result += number_of_last_letter
    new_list.append(result)

final_result = 0
for i in new_list:
    final_result += float(i)
print(f"{final_result:.2f}")