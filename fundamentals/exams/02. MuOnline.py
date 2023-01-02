rooms = input().split("|")

room = 0
health = 100
current_health = 0
bitcoins = 0
killed = False
for i in rooms:
    command, value = i.split()
    number = int(value)
    room += 1
    if command == "potion":
        current_health = health + number
        if current_health > 100:
            needed_health = 100 - health
            health = 100
            print(f"You healed for {needed_health} hp.")
            print(f"Current health: {health} hp.")
        elif 0 < current_health <= 100:
            health = current_health
            print(f"You healed for {number} hp.")
            print(f"Current health: {health} hp.")
    elif command == "chest":
        bitcoins += number
        print(f"You found {number} bitcoins.")
    else:
        health -= number
        if health > 0:
            print(f"You slayed {command}.")
        elif health <= 0:
            print(f"You died! Killed by {command}.")
            killed = True
            print(f"Best room: {room}")
            break
if not killed:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
