data = input()

first_dict = {}
user_exists = False
while data != "Lumpawaroo":
    user_exists = False
    if " | " in data:
        side, user = data.split(" | ")
        for i in first_dict.values():
            if user in i:
                user_exists = True
                break
        if not user_exists:
            if side not in first_dict:
                first_dict[side] = []
            first_dict[side].append(user)
    elif " -> " in data:
        user, side = data.split(" -> ")
        for i in first_dict.values():
            if user in i:
                user_exists = True
                break
        if not user_exists:
            if side not in first_dict:
                first_dict[side] = []
            first_dict[side].append(user)
            print(f"{user} joins the {side} side!")
        elif user_exists:
            for key, value in first_dict.items():
                if user in value:
                    first_dict[key].remove(user)
                    if side not in first_dict:
                        first_dict[side] = []
                    first_dict[side].append(user)
                    print(f"{user} joins the {side} side!")
                    break
    data = input()

for side, users in sorted(first_dict.items(), key=lambda x: (-len(x[1]), x[0])):
    if len(users) == 0:
        continue
    else:
        print(f"Side: {side}, Members: {len(users)}")
    for j in sorted(users):
        print(f"! {j}")