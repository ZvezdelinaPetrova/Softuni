genres = input().split(" | ")

command = input()

while command != "Stop!":
    command = command.split()
    if command[0] == "Join":
        if command[1] not in genres:
            genres.append(command[1])
    elif command[0] == "Drop":
        if command[1] in genres:
            while command[1] in genres:
                genres.remove(command[1])
    elif command[0] == "Replace":
        if command[1] in genres and command[2] not in genres:
            old_genre = genres.index(command[1])
            new_genre = genres.index(command[1])
            genres.pop(old_genre)
            genres.insert(old_genre, command[2])
    command = input()

print(*genres, sep=" ")