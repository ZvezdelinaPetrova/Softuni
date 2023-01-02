n = int(input())

even = 0
odd = 0

for e in range(1, n + 1):
    number = int(input())
    if e % 2 == 0:
        even = even + number
    else:
        odd = odd + number

if even == odd:
    print(f"Yes")
    print(f"Sum = {even}")
else:
    difference = abs(even - odd)
    print(f"No")
    print(f"Diff = {difference}")
