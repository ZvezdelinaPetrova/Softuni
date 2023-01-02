words = [el.lower() for el in input().split()]

words_dict = {}

for i in words:
    if i not in words_dict:
        words_dict[i] = 0
    words_dict[i] += 1

for key, value in words_dict.items():
    if value % 2 == 1:
        print(f"{key}", end=" ")