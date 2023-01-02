data = [float(i) for i in input().split()]

new_list = {}

for i in data:
    if i in new_list:
        new_list[i] += 1
    else:
        new_list[i] = 1

for key, value in new_list.items():
    print(f"{key} - {value} times")