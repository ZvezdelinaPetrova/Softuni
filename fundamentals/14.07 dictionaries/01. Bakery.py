bakery = input().split()

new_dict = {}

for i in range(0, len(bakery), 2):
    key = bakery[i]
    value = int(bakery[i + 1])
    new_dict[key] = value

print(new_dict)