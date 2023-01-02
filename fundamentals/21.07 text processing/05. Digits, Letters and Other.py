text = input()

digits = ""
letters = ""
symbols = ""

for i in text:
    if i.isdigit():
        digits += i
    elif i.isalpha():
        letters += i
    else:
        symbols += i
print(digits)
print(letters)
print(symbols)