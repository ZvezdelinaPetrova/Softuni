activation_key = input()
command_line = input()

while not command_line == 'Generate':
    command_line = command_line.split('>>>')
    command = command_line[0]
    if command == 'Contains':
        substring = command_line[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")
    elif command == 'Flip':
        up_low = command_line[1]
        start_ind = int(command_line[2])
        end_ind = int(command_line[3])
        if up_low == 'Upper':
            activation_key = activation_key[:start_ind] + activation_key[start_ind:end_ind].upper() + activation_key[
                                                                                                      end_ind:]
        elif up_low == 'Lower':
            activation_key = activation_key[:start_ind] + activation_key[start_ind:end_ind].lower() + activation_key[
                                                                                                      end_ind:]
        print(activation_key)
    elif command == 'Slice':
        start_ind = int(command_line[1])
        end_ind = int(command_line[2])
        substring = activation_key[start_ind:end_ind]
        activation_key = activation_key.replace(substring, '')
        print(activation_key)
    command_line = input()

print(f"Your activation key is: {activation_key}")