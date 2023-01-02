message = input()
command_line = input()

while not command_line == 'Reveal':
    command_line = command_line.split(':|:')
    command = command_line[0]
    if command == 'InsertSpace':
        ind = int(command_line[1])
        message = message[:ind] + ' ' + message[ind:]
        print(message)
    elif command == 'Reverse':
        substring = command_line[1]
        if substring in message:
            reversed_substring = substring[::-1]
            message = message.replace(substring, '', 1)
            message = message + reversed_substring
            print(message)
        else:
            print('error')
    elif command == 'ChangeAll':
        substring = command_line[1]
        replacement_string = command_line[2]
        message = message.replace(substring, replacement_string)
        print(message)

    command_line = input()

print(f"You have a new text message: {message}")