text = input()

vowels = ['a', 'o', 'u', 'e', 'i', 'A', 'O', 'U', 'E', 'I']

new_word = [el for el in text if el not in vowels]

# for i in text:
#     if i in vowels:
#         continue
#     else:
#         new_word.append(i)
print(*new_word, sep='')
