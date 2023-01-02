data = input()


new_dict = {}

while data != "stop":
    key = data
    value = int(input())
    if key not in new_dict:
        new_dict[key] = value
    elif data in new_dict:
        new_dict[key] += value
    data = input()

for key, value in new_dict.items():
    print(f"{key} -> {value}")