scrabble = input()

command = input()

while command != "Play" and command != "Pass":
    command = command.split()
    action = command[0]
    if action == "Move":
        index = int(command[1])
        if 0 <= index < len(scrabble):
            letter = scrabble[index]
            scrabble = scrabble[:index] + scrabble[index + 1:] + letter
    elif action == "Insert" and command[1] == "Space":
        index = int(command[2])
        scrabble = scrabble[:index] + " " + scrabble[index:]
    elif action == "Reverse":
        substring = command[1]
        if substring in scrabble:
            reversed_substring = substring[::-1]
            scrabble = scrabble.replace(substring, "", 1)
            scrabble = scrabble + reversed_substring
    elif action == "Exchange" and command[1] == "Tiles":
        new_letters = command[2]
        how_many = len(new_letters)
        scrabble = scrabble[how_many:]
        scrabble = new_letters + scrabble
        print(" ".join(scrabble))
        break

    command = input()

if command == "Play":
    if " " not in scrabble:
        print(f"You are playing with the word {scrabble}.")
    else:
        new_word = ""
        for i in scrabble:

            if i == " ":
                break
            else:
                new_word += i
        print(f"You are playing with the word {new_word}.")
    exit()

if command == "Pass":
    print(" ".join(scrabble))
    exit()
