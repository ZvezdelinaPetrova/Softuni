data = input().split()

total = 0

word_1 = data[0]
word_2 = data[1]
word_min = min(len(word_1), len(word_2))

for j in range(word_min):
    as_number = ord(word_1[j])
    as_number_second = ord(word_2[j])
    total += as_number * as_number_second

if len(word_1) > len(word_2):
    letters_1 = word_1[word_min:]
    for m in letters_1:
        letter_to_covert = ord(m)
        total += letter_to_covert
elif len(word_1) < len(word_2):
    letters_2 = word_2[word_min:]
    for g in letters_2:
        letter_to_covert = ord(g)
        total += letter_to_covert

print(total)