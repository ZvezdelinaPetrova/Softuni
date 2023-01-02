width = int(input())
height = int(input())
new_command = input()

counter = 0
whole_cake = width * height
cake_is_over = False

while new_command != "STOP":
    command = int(new_command)
    counter += command
    if counter > whole_cake:
        cake_is_over = True
        break
    new_command = input()

difference = abs(counter - whole_cake)
if cake_is_over:
    print(f"No more cake left! You need {difference} pieces more.")
else:
    print(f"{difference} pieces are left.")


