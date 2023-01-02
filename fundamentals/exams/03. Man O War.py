pirates = [int(el) for el in input().split(">")]
warship = [int(el) for el in input().split(">")]
max_health = int(input())

command = input()
sunken = False

while command != "Retire":
    command = command.split()
    if command[0] == "Fire":
        index = int(command[1])
        damage = int(command[2])
        if 0 <= index < len(warship):
            warship[index] -= damage
            if warship[index] <= 0:
                print("You won! The enemy ship has sunken.")
                sunken = True
                break
    elif command[0] == "Defend":
        start_index = int(command[1])
        end_index = int(command[2])
        attack_of_the_warship = int(command[3])
        if 0 <= start_index < len(pirates) and 0 <= end_index < len(pirates):
            for i in range(start_index, end_index + 1):
                pirates[i] -= attack_of_the_warship
                if pirates[i] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    sunken = True
                    break
    elif command[0] == "Repair":
        index = int(command[1])
        recovery = int(command[2])
        if 0 <= index < len(pirates):
            if pirates[index] + recovery <= max_health:
                pirates[index] = pirates[index] + recovery
            else:
                pirates[index] = max_health
    elif command[0] == "Status":
        counter = 0
        minimum_health = max_health * 0.2
        for i in pirates:
            if i < minimum_health:
                counter += 1
        print(f"{counter} sections need repair.")
    command = input()

if not sunken:
    pirate_sum = sum(pirates)
    warship_sum = sum(warship)
    print(f"Pirate ship status: {pirate_sum}")
    print(f"Warship status: {warship_sum}")