elements = [el for el in input().split()]

moves = 0
won = False
command = input()

while command != "end":
    moves += 1
    index_1, index_2 = command.split()
    index_1 = int(index_1)
    index_2 = int(index_2)
    if 0 <= index_1 < len(elements) and 0 <= index_2 < len(elements):
        if elements[index_1] == elements[index_2]:
            print(f"Congrats! You have found matching elements - {elements[index_1]}!")
            item_to_delete = elements[index_1]
            while item_to_delete in elements:
                elements.remove(item_to_delete)
            # element_to_delete_1 = elements.pop(index_1)
            # elements.remove(element_to_delete_1)
        else:
            print("Try again!")
    elif not 0 <= index_1 < len(elements) or not 0 <= index_2 < len(elements):
        middle = int(len(elements) / 2)
        element_to_add = f"-{moves}a"
        elements.insert(middle, element_to_add)
        elements.insert(middle, element_to_add)
        print(f"Invalid input! Adding additional elements to the board")
    elif index_1 == index_2:
        middle = len(elements) // 2
        element_to_add = f"-{moves}a"
        elements.insert(middle, element_to_add)
        elements.insert(middle, element_to_add)
        print(f"Invalid input! Adding additional elements to the board")
    if len(elements) == 0:
        won = True
        print(f"You have won in {moves} turns!")
        break
    command = input()

if not won:
    print(f"Sorry you lose :(")
    print(*elements, sep=" ")
# if command == "end":
#     print(f"Sorry you lose :(")
#     print(*elements, sep=" ")
