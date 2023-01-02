n = int(input())

first = 0
second = 0
third = 0
forth = 0

for i in range(1111, 10000):
    number = str(i)
    for index, digit in enumerate(number):
        if digit == "0":
            continue
        if index == 0:
            first = int(digit)
        elif index == 1:
            second = int(digit)
        elif index == 2:
            third = int(digit)
        elif index == 3:
            forth = int(digit)
    if n % first == 0 and n % second == 0 and n % third == 0 and n % forth == 0:
        print(f"{first}{second}{third}{forth}", end=" ")


