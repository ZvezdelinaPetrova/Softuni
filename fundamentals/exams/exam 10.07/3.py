command = input()

chat = []
while command != "end":
    command = command.split()
    if command[0] == "Chat":
        chat.append(command[1])
    elif command[0] == "Delete":
        if command[1] in chat:
            while command[1] in chat:
                chat.remove(command[1])
    elif command[0] == "Edit":
        if command[1] in chat:
            old_message = chat.index(command[1])
            chat.pop(old_message)
            chat.insert(old_message, command[2])
    elif command[0] == "Pin":
        if command[1] in chat:
            index_of_message_to_find = chat.index(command[1])
            chat.pop(index_of_message_to_find)
            chat.append(command[1])
    elif command[0] == "Spam":
        new_list = command[1:]
        for i in new_list:
            chat.append(i)
    command = input()

for messages in chat:
    print(messages)