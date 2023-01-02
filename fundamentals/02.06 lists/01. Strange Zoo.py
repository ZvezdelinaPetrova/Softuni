first = input()
second = input()
third = input()

animal = [first, second, third]

animal[2], animal[0] = animal[0], animal[2]

print(animal)