to_do_list = ["0"] * 11

command = input()

while command != "End":
    new_action = command.split("-")
    item_to_add = new_action[1]
    index = int(new_action[0])
    to_do_list.pop(index)
    to_do_list.insert(index, item_to_add)
    command = input()

# while "0" in to_do_list:
#     to_do_list.remove("0")
result = [el for el in to_do_list if el != "0"]
print(result)
