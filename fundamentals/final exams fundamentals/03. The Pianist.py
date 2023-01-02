num = int(input())
collection = {}

for _ in range(num):
    piece, composer, key = input().split("|")
    collection[piece] = [composer, key]

command_line = input()

while not command_line == 'Stop':
    command_line = command_line.split("|")
    command = command_line[0]
    piece = command_line[1]
    if command == 'Add':
        composer = command_line[2]
        key = command_line[3]
        if piece in collection:
            print(f"{piece} is already in the collection!")
        else:
            collection[piece] = [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")
    elif command == 'Remove':
        if piece in collection:
            collection.pop(piece)
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif command == 'ChangeKey':
        if piece in collection:
            new_key = command_line[2]
            collection[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    command_line = input()

sorted_collection = dict(sorted(collection.items(), key=lambda kvp: (kvp[0], kvp[1][0])))

for key, value in sorted_collection.items():
    print(f"{key} -> Composer: {value[0]}, Key: {value[1]}")