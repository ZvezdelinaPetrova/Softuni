n = int(input())

even = []
odd =[]
negative = []
positive = []

for i in range(n):
    new_number = int(input())
    if new_number % 2 == 0:
        even.append(new_number)
    if new_number % 2 == 1:
        odd.append(new_number)
    if new_number >= 0:
        positive.append(new_number)
    if new_number < 0:
        negative.append(new_number)
word = input()

if word == "even":
    print(even)
elif word == "odd":
    print(odd)
elif word == "negative":
    print(negative)
elif word == "positive":
    print(positive)
