import sys
n = int(input())
num = 0
max_num = - sys.maxsize
total = 0
for i in range(n):
    num = int(input())
    if max_num < num:
        max_num = num
    total = total + num
if max_num == total - max_num:
    print("Yes")
    print(f"Sum = {max_num}")
else:
    difference = abs(max_num - (total - max_num))
    print(f"No")
    print(f"Diff = {difference}")



