command = input()

all_simple = 0
all_not_simple = 0
while command != "stop":
    new_number = int(command)
    if new_number > 3 and new_number % 3 == 0:
        all_not_simple += new_number
    elif new_number > 3 and new_number % 2 == 0:
        all_not_simple += new_number
    elif new_number < 0:
        print(f"Number is negative.")
    else:
        all_simple += new_number
    command = input()

print(f"Sum of all prime numbers is: {all_simple}")
print(f"Sum of all non prime numbers is: {all_not_simple}")
