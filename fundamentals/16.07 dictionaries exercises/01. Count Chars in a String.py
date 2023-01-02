word = input().split(" ")

word_dict = {}

for el in word:
    for i in el:
        if i not in word_dict:
            word_dict[i] = 1
        elif i in word_dict:
            word_dict[i] += 1
for key, value in word_dict.items():
    print(f"{key} -> {value}")
