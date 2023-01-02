command = input()

new_dict = {}

while command != "Results":
    command = command.split(":")
    action = command[0]
    name = command[1]
    if action == "Add":
        health = int(command[2])
        energy = int(command[3])
        if name not in new_dict:
            new_dict[name] = {'health': health, 'energy': energy}
        else:
            new_dict[name]['health'] += health
    elif action == "Attack":
        name_2 = command[2]
        damage = int(command[3])
        if name in new_dict and name_2 in new_dict:
            new_dict[name_2]['health'] -= damage
            new_dict[name]['energy'] -= 1
        if new_dict[name_2]['health'] <= 0:
            new_dict.pop(name_2)
            print(f"{name_2} was disqualified!")
        if new_dict[name]['energy'] <= 0:
            new_dict.pop(name)
            print(f"{name} was disqualified!")
    elif action == "Delete":
        if name in new_dict:
            new_dict.pop(name)
        if name == "All":
            new_dict.clear()

    command = input()

print(f"People count: {len(new_dict)}")

sorted_something = sorted(new_dict.items(), key=lambda kvp: (-kvp[1]["health"], kvp[0]))

for key, values in sorted_something:
    health = values["health"]
    energy = values["energy"]
    print(f"{key} - {health} - {energy}")

