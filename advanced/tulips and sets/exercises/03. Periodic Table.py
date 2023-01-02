n = int(input())

new_set = set()

for _ in range(n):
    data = input().split()
    for i in data:
        new_set.add(i)

for j in new_set:
    print(j)