from collections import deque


effect = deque(int(x) for x in input().split(", "))  # first
casings = deque(int(x) for x in input().split(", "))  # last

bombs = {
    "Datura Bombs": 40,
    "Cherry Bombs": 60,
    "Smoke Decoy Bombs": 120
}
success = False
collected = {
    "Datura Bombs": 0,
    "Cherry Bombs": 0,
    "Smoke Decoy Bombs": 0}
found = False
while effect and casings:
    found = False
    current_effect = effect.popleft()
    current_casing = casings.pop()
    result = current_effect + current_casing
    for key, value in bombs.items():
        if result == value:
            found = True
            collected[key] += 1
    if not found:
        casings.append(current_casing - 5)
        effect.appendleft(current_effect)
    if collected["Datura Bombs"] >= 3 and \
            collected["Cherry Bombs"] >= 3 and collected["Smoke Decoy Bombs"] >= 3:
        success = True
        break

if success:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print(f"You don't have enough materials to fill the bomb pouch.")

if effect:
    print(f"Bomb Effects: {', '.join(str(x) for x in effect)}")
else:
    print(f"Bomb Effects: empty")
if casings:
    print(f"Bomb Casings: {', '.join(str(x) for x in casings)}")
else:
    print(f"Bomb Casings: empty")


for k, v in sorted(collected.items()):
    print(f"{k}: {v}")


# from collections import deque
#
# bombs = {
#     60: 0,
#     40: 0,
#     120: 0
# }
#
# bomb_effects = deque([int(el) for el in input().split(', ')])
# bomb_casings = [int(el) for el in input().split(', ')]
# full_pouch = False
#
# while bomb_casings and bomb_effects:
#     first_bomb_effect = bomb_effects[0]
#     last_bomb_casing = bomb_casings[-1]
#     bomb = first_bomb_effect + last_bomb_casing
#
#     if bomb == 40 or bomb == 60 or bomb == 120:
#         bomb_effects.popleft()
#         bomb_casings.pop()
#         bombs[bomb] += 1
#     else:
#         bomb_casings[-1] -= 5
#
#     if bombs[40] >= 3 and bombs[60] >= 3 and bombs[120] >= 3:
#         full_pouch = True
#         break
#
# if not full_pouch:
#     print(f"You don't have enough materials to fill the bomb pouch.")
# else:
#     print(f"Bene! You have successfully filled the bomb pouch!")
#
# if not bomb_effects:
#     print(f"Bomb Effects: empty")
# else:
#     print(f"Bomb Effects: {', '.join([str(el) for el in bomb_effects])}")
#
# if not bomb_casings:
#     print(f"Bomb Casings: empty")
# else:
#     print(f"Bomb Casings: {', '.join([str(el) for el in bomb_casings])}")
#
# for key, value in bombs.items():
#     if key == 60:
#         print(f"Cherry Bombs: {value}")
#     elif key == 40:
#         print(f"Datura Bombs: {value}")
#     else:
#         print(f"Smoke Decoy Bombs: {value}")


















