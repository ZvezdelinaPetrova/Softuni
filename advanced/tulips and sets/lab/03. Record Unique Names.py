n = int(input())

new_list = []

for _ in range(n):
    name = input()
    new_list.append(name)

set_test = set(new_list)

for el in set_test:
    print(el)