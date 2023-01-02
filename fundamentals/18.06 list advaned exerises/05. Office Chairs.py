number = int(input())

room = 0
total_free = 0
game_on = True

for i in range(1, number + 1):
    room += 1
    chairs, people = input().split()
    needed_chairs = 0
    if len(chairs) < int(people):
        difference = abs(int(people) - len(chairs))
        needed_chairs += difference
        print(f"{needed_chairs} more chairs needed in room {room}")
        game_on = False
    elif len(chairs) >= int(people):
        difference = len(chairs) - int(people)
        total_free += difference

if game_on:
    print(f"Game On, {total_free} free chairs left")

