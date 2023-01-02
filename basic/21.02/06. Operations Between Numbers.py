N1 = int(input())
N2 = int(input())
symbol = input()

result = ""
number = ""
odd_or_even = "odd"

if symbol == "+" or symbol == "-" or symbol == "*":
    if symbol == "+":
        result = N1 + N2
    elif symbol == "-":
        result = N1 - N2
    elif symbol == "*":
        result = N1 * N2
    if result % 2 == 0:
        number = "even"
    elif result % 2 == 1:
        number = "odd"
    print(f"{N1} {symbol} {N2} = {result} - {number}")
elif symbol == "%" or symbol == "/":
    if symbol == "%" and N2 == 0:
        print(f"Cannot divide {N1} by zero")
    elif symbol == "/" and N2 == 0:
        print(f"Cannot divide {N1} by zero")
    elif symbol == "%" and N2 != 0:
        result = N1 % N2
        print(f"{N1} % {N2} = {result}")
    elif symbol == "/" and N1 != 0:
        result = N1 / N2
        print(f"{N1} {symbol} {N2} = {result:.2f}")



# moje i tova s delenieto na 0 da go napiseh
# if N2 == 0 printirame che ne moje da se izpalni