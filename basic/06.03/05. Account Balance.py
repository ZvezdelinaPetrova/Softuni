command = input()

total = 0

while command != "NoMoreMoney":
    command = float(command)
    if command < 0:
        print("Invalid operation!")
        break
    print(f"Increase: {command:.2f}")
    total += command
    command = input()
print(f"Total: {total:.2f}")


