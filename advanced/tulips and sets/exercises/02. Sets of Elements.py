n, m = input().split()
n = int(n)
m = int(m)

first_set = set()
second_set = set()

for _ in range(n):
    first = input()
    first_set.add(first)
for _ in range(m):
    second = input()
    second_set.add(second)

same_numbers = first_set.intersection(second_set)

for i in same_numbers:
    print(i)