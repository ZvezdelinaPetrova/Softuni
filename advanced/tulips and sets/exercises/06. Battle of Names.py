from math import floor

n = int(input())

odd_set = set()
even_set = set()

for x in range(n):
    sum_all = 0
    current_row = x + 1
    current_name = input()
    for j in current_name:
        ch = ord(j)
        sum_all += ch
    result = floor(sum_all / current_row)
    if result % 2 == 1:
        odd_set.add(result)
    else:
        even_set.add(result)

if sum(odd_set) == sum(even_set):
    result = odd_set.union(even_set)
    print(f"{', '.join(str(x) for x in result)}")

if sum(odd_set) > sum(even_set):
    result = odd_set.difference(even_set)
    print(f"{', '.join(str(x) for x in result)}")

if sum(odd_set) < sum(even_set):
    result = odd_set.symmetric_difference(even_set)
    print(f"{', '.join(str(x) for x in result)}")

# n = int(input())
#
# even_set = set()
# odd_set = set()
#
# for j in range(1, n + 1):
#     total = 0
#     name = input()
#     for i in name:
#         total += ord(i)
#     total = total // j
#     if total % 2 == 0:
#         even_set.add(total)
#     elif total % 2 == 1:
#         odd_set.add(total)
#
# even_total = sum(even_set)
# odd_total = sum(odd_set)
#
#
# result = set()
#
# if even_total == odd_total:
#     result = odd_set.union(even_set)
# elif even_total < odd_total:
#     result = odd_set.difference(even_set)
# elif even_total > odd_total:
#     result = odd_set.symmetric_difference(even_set)
#
# print(", ".join(str(i) for i in result))