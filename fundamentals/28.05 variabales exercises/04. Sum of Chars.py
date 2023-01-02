n = int(input())

counter = 0

for i in range(n):
    symbol = input()
    number_of_symbol = ord(symbol)
    counter += number_of_symbol

print(f"The sum equals: {counter}")