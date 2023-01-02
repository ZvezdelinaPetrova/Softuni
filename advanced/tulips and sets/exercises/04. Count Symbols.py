text = [i for i in input()]

new_dict = {}

for i in text:
    if i not in new_dict:
        new_dict[i] = 1
    else:
        new_dict[i] += 1

for key, value in sorted(new_dict.items()):
    print(f"{key}: {value} time/s")