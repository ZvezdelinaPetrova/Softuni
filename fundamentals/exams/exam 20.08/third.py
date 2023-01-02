command = input()

new_dict = {}

while command != "End":
    command = command.split()
    action = command[0]
    name = command[1]
    if action == "Enroll":
        if name not in new_dict:
            new_dict[name] = []
        else:
            print(f"{name} is already enrolled.")
    elif action == "Learn":
        spell_name = command[2]
        if name not in new_dict:
            print(f"{name} doesn't exist.")
        else:
            if spell_name in new_dict[name]:
                print(f"{name} has already learnt {spell_name}.")
            else:
                new_dict[name].append(spell_name)

    elif action == "Unlearn":
        spell = command[2]
        if name not in new_dict:
            print(f"{name} doesn't exist.")
        else:
            if spell not in new_dict[name]:
                print(f"{name} doesn't know {spell}.")
            else:
                new_dict[name].remove(spell)
    command = input()

test = []
print("Heroes:")
new_dict = sorted(new_dict.items(), key=lambda x: (-len(x[1]), x[0]))
for key, value in new_dict:
    if len(value) == 0:
        print(f"== {key}:")
    else:
        print(f"== {key}: {', '.join(value)}")
