resources = input().split(", ")

command = input()

while command != "Craft!":
    new_command, item = command.split(" - ")
    if new_command == "Collect":
        if item not in resources:
            resources.append(item)
    elif new_command == "Drop":
        if item in resources:
            resources.remove(item)
    elif new_command == "Combine Items":
        new_list = item.split(":")
        if new_list[0] in resources:
            index = resources.index(new_list[0])
            resources.insert(index + 1, new_list[1])
    elif new_command == "Renew":
        if item in resources:
            resources.append(item)
            resources.remove(item)

    command = input()

print(", ".join(resources))
#print(*resources, sep =", ")