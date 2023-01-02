n = int(input())

new_dict = {}

for _ in range(n):
    data = input().split()
    name = data[0]
    grade = float(data[1])
    if name not in new_dict:
        new_dict[name] = []
    new_dict[name].append(grade)


for key, value in new_dict.items():
    unpacked_list = " ".join(str(f'{x:.2f}') for x in value)
    print(f"{key} -> {unpacked_list} (avg: {sum(value) / len(value):.2f})")
    # new_list = []
    # for x in value:
    #     test = f"{x:.2f}"
    #     new_list.append(test)
    # print(f"{key} -> {' '.join(x for x in new_list)} (avg: {sum(value) / len(value):.2f})")