command = input()

number_of_adults = 0
number_of_kids = 0
toys = 0
sweaters = 0

while command != "Christmas":
    new_command = int(command)
    if new_command <= 16:
        number_of_kids += 1
        toys += 1
    elif new_command > 16:
        number_of_adults += 1
        sweaters += 1
    command = input()
money_for_toys = toys * 5
money_for_sweaters = sweaters * 15

print(f"Number of adults: {number_of_adults}")
print(f"Number of kids: {number_of_kids}")
print(f"Money for toys: {money_for_toys}")
print(f"Money for sweaters: {money_for_sweaters}")
