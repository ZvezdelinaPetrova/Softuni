password = input()
command_line = input()

while not command_line == 'Done':
    command_line = command_line.split()
    command = command_line[0]
    if command == 'TakeOdd':
        new_pass = ''
        for ind in range(1, len(password), 2):
            new_pass += password[ind]
        password = new_pass
        print(password)
    elif command == 'Cut':
        ind = int(command_line[1])
        length = int(command_line[2])
        substring = password[ind:ind + length]
        password = password.replace(substring, '', 1)
        print(password)
    elif command == 'Substitute':
        substring = command_line[1]
        substitute = command_line[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")
    command_line = input()

print(f"Your password is: {password}")