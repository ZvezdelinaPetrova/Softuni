first = int(input())
second = int(input())

even_counter = 0
odd_counter = 0

for i in range(first, second + 1):
    number = str(i)
    even_counter = 0
    odd_counter = 0
    for index, digit in enumerate(number):
        if index % 2 == 0:
            even_counter += int(digit)
        if index % 2 == 1:
            odd_counter += int(digit)
    if even_counter == odd_counter:
        print(number, end=" ")


