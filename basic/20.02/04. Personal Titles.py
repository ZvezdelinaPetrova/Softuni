age = float(input())
sex = input()

if age >= 16:
    if sex == "f":
        print("Ms.")
    elif sex == "m":
        print("Mr.")
else:
    if sex == "f":
        print("Miss")
    elif sex == "m":
        print("Master")
