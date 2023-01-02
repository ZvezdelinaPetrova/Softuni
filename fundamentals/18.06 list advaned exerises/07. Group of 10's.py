numbers = [int(el) for el in input().split(", ")]

group = 10
list_of_numbers = []

while len(numbers) > 0:
    list_of_numbers = []
    for el in numbers:
        if el <= group:
            list_of_numbers.append(el)
    print(f"Group of {group}'s: {list_of_numbers}")

    for i in list_of_numbers:
        if i in numbers:
            numbers.remove(i)
    group += 10
