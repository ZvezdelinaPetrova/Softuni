treasures = input().split("|")

command = input()
counter = 0
new_list = []
items = []

while command != "Yohoho!":
    command_split = command.split()
    if command_split[0] == "Loot":
        items = command_split[1:]
        for i in items:
            if i not in treasures:
                treasures.insert(0, i)
    elif command_split[0] == "Drop":
        index = int(command_split[1])
        if abs(index) < len(treasures):
            item = treasures.pop(index)
            treasures.append(item)
    elif command_split[0] == "Steal":
        count = int(command_split[1])
        if len(treasures) >= count:
            count_to_delete = len(treasures) - count
            new_list = treasures[count_to_delete:]
            print(*new_list, sep=", ")
            treasures = treasures[0:count_to_delete]
        elif count > len(treasures):
            new_list = treasures
            print(*new_list, sep=", ")
            treasures.clear()
        if len(treasures) == 0:
            break

    command = input()

if len(treasures) > 0:
    for j in treasures:
        counter += len(j)
    average = counter / len(treasures)
    print(f"Average treasure gain: {average:.2f} pirate credits.")
elif len(treasures) == 0:
    print("Failed treasure hunt.")
