n = int(input())

new_dict = {}
final_dict = {}
for i in range(n):
    name = input()
    grade = float(input())
    if name not in new_dict:
        new_dict[name] = []
        new_dict[name].append(grade)
    else:
        new_dict[name].append(grade)

for name, values in new_dict.items():
    new_dict[name] = sum(new_dict[name]) / len(new_dict[name])

for name, value in new_dict.items():
    if value >= 4.5:
        final_dict[name] = value

final_dict = sorted(final_dict.items(), key=lambda kvp: -kvp[1])
for key, value in final_dict:
    print(f"{key} -> {value:.2f}")