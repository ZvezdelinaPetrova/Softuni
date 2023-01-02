day_events = input().split("|")
energy = 100
coins = 100

day_not_completed = True

for event in day_events:
    split_event = event.split("-")
    current_event = split_event[0]
    current_number = int(split_event[1])
    if current_event == "rest":
        if energy >= 100:
            current_number = 0
        if current_number + energy <= 100:
            energy += current_number
        print(f"You gained {current_number} energy.")
        print(f"Current energy: {energy}.")
    elif current_event == "order":
        if energy - 30 >= 0:
            coins += current_number
            energy -= 30
            print(f"You earned {current_number} coins.")
        elif energy < 30:
            energy += 50
            print("You had to rest!")
    else:
        if coins - current_number > 0:
            coins -= current_number
            print(f"You bought {current_event}.")
        elif coins - current_number <= 0:
            day_not_completed = False
            print(f"Closed! Cannot afford {current_event}.")
            break

if day_not_completed:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")


