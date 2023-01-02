code = input()
message = input()
decrypted_message = ''

while not message == 'Decode':
    message = message.split('|')
    command = message[0]
    if command == 'Move':
        number = int(message[1])
        code = code[number:] + code[:number]
    elif command == 'Insert':
        ind = int(message[1])
        val = message[2]
        code = code[:ind] + val + code[ind:]
    elif command == 'ChangeAll':
        old_str = message[1]
        new_str = message[2]
        code = code.replace(old_str, new_str)
    message = input()

print(f"The decrypted message is: {code}")