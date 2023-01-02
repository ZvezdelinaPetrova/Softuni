command = input()

goal = 10000
steps = 0

while command != "Going home":
    new_command = int(command)
    steps += new_command
    if steps >= goal:
        break
    command = input()


if command == "Going home":
    new_command = int(input())
    steps += new_command

difference = abs(steps - goal)

if steps >= goal:
    print("Goal reached! Good job!")
    print(f"{difference} steps over the goal!")
else:
    print(f"{difference} more steps to reach goal.")