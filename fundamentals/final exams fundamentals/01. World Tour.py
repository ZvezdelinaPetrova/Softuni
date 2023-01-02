stops = input()

command_line = input()

while not command_line == 'Travel':
    command_line = command_line.split(':')
    command = command_line[0]
    if command == 'Add Stop':
        ind, text = command_line[1:]
        if int(ind) in range(len(stops)):
            stops = stops[:int(ind)] + text + stops[int(ind):]
        print(stops)
    elif command == 'Remove Stop':
        start_ind, end_ind = command_line[1:]
        if int(start_ind) in range(len(stops)) and int(end_ind) in range(len(stops)):
            stops = stops[:int(start_ind)] + stops[int(end_ind) + 1:]
        print(stops)
    elif command == 'Switch':
        old_str, new_str = command_line[1:]
        if old_str in stops:
            stops = stops.replace(old_str, new_str)
        print(stops)
    command_line = input()

print(f"Ready for world tour! Planned stops: {stops}")