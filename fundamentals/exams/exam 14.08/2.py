username = input()
command = input()

while command != "Registration":
    command = command.split()
    action = command[0]
    if action == "Letters":
        if command[1] == "Lower":
            username = username.lower()
            print(f"{username}")
        elif command[1] == "Upper":
            username = username.upper()
            print(f"{username}")
    elif action == "Reverse":
        start_index = int(command[1])
        end_index = int(command[2])
        if 0 <= start_index < len(username) and 0 <= end_index < len(username):
            reverse_text = username[end_index: start_index - 1: -1]
            print(reverse_text)
            # if start <= len(username) and end <= len(username):
            #     x = username[start:end + 1]
            #     y = x[::-1]
            #     print(y)
    elif action == "Substring":
        thing_to_delete = command[1]
        if thing_to_delete in username:
            username = username.replace(thing_to_delete, "")
            print(f"{username}")
        else:
            print(f"The username {username} doesn't contain {thing_to_delete}.")
    elif action == "Replace":
        char_to_delete = command[1]
        if char_to_delete in username:
            username = username.replace(char_to_delete, "-")
            print(f"{username}")
    elif action == "IsValid":
        char_to_find = command[1]
        if char_to_find in username:
            print(f"Valid username.")
        elif char_to_find not in username:
            print(f"{char_to_find} must be contained in your username.")
    command = input()



