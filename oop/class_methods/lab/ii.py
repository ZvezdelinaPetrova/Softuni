rooms = [1, 2, 3]


def take_room(room_number, people):
    room = [r for r in rooms if r == room_number]
    print("Executed", room, type(room))


print(take_room(1, 1))