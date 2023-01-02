width = int(input())
length = int(input())
height = int(input())

space = width * length * height
used_space = 0
is_space_used = False
command = input()

while command != "Done":
    command = int(command)
    if used_space < space:
        used_space = used_space + command
    if used_space > space:
        is_space_used = True
        break
    command = input()
difference = abs(space - used_space)

if is_space_used:
    print(f"No more free space! You need {difference} Cubic meters more.")
else:
    print(f"{difference} Cubic meters left.")
