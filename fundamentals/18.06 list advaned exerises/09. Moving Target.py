targets = [int(el) for el in input().split()]

command = input()

while command != "End":
    action, index, number = command.split()
    index = int(index)
    number = int(number)
    if action == "Shoot":
        if 0 <= index < len(targets):
            targets[index] -= number
            if targets[index] <= 0:
                targets.pop(index)
    elif action == "Add":
        if 0 <= index < len(targets):
            targets.insert(index, number)
        else:
            print("Invalid placement!")
    elif action == "Strike":
        beginning = index - number
        end = index + number
        if (0 <= index < len(targets)) and (0 <= beginning < index) and (index < end <= len(targets)):
            del targets[beginning: end + 1]
        else:
            print("Strike missed!")

    command = input()
print(*targets, sep="|")