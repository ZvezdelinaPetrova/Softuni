n = int(input())

positive = []
negative = []

total_positive = 0
count_negative = 0

for i in range(n):
    new_number = int(input())
    if new_number >= 0:
        positive.append(new_number)
        total_positive += 1
    elif new_number < 0:
        negative.append(new_number)
        count_negative += new_number

print(positive)
print(negative)

print(f"Count of positives: {total_positive}. Sum of negatives: {count_negative}")