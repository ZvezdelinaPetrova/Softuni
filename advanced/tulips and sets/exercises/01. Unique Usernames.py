n = int(input())

new_set = set()

for _ in range(n):
    name = input()
    new_set.add(name)

for i in new_set:
    print(i)