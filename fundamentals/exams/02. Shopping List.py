products = input().split("!")

command = input()

while command != "Go Shopping!":
    split_command = command.split()
    action = split_command[0]
    item = split_command[1]
    if action == "Urgent":
        if item not in products:
            products.insert(0, item)
    elif action == "Unnecessary":
        if item in products:
            products.remove(item)
    elif action == "Correct":
        if item in products:
            item_index = products.index(item)
            products.pop(item_index)
            products.insert(item_index, split_command[2])
    elif action == "Rearrange":
        if item in products:
            item_index = products.index(item)
            products.pop(item_index)
            products.append(item)
    command = input()
print(*products, sep=", ")