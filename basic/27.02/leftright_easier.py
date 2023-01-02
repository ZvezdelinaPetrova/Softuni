n = int(input())

left_sum = 0
right_sum = 0

for l_s in range(n):
    numbers = int(input())
    left_sum = left_sum + numbers
for r in range(n):
    numbers = int(input())
    right_sum = right_sum + numbers
if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    difference = abs(left_sum - right_sum)
    print(f"No, diff = {difference}")
