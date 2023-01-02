from collections import deque


fireworks = deque(int(x) for x in input().split(", "))  # first
power = deque(int(x) for x in input().split(", "))  # last

collected = {
    "Palm Fireworks": 0,
    "Willow Fireworks": 0,
    "Crossette Fireworks": 0
}
success = False
while fireworks and power:
    current_firework = fireworks.popleft()
    current_power = power.pop()
    if current_firework <= 0:
        power.append(current_power)
        continue
    if current_power <= 0:
        fireworks.appendleft(current_firework)
        continue
    result = current_firework + current_power
    if result % 3 == 0 and result % 5 == 0:
        collected["Crossette Fireworks"] += 1
    elif result % 3 == 0:
        collected["Palm Fireworks"] += 1
    elif result % 5 == 0:
        collected["Willow Fireworks"] += 1
    else:
        fireworks.append(current_firework - 1)
        power.append(current_power)
    if collected["Crossette Fireworks"] >= 3 and \
            collected["Palm Fireworks"] >= 3 and collected["Willow Fireworks"] >= 3:
        success = True
        break

if success:
    print(f"Congrats! You made the perfect firework show!")
else:
    print(f"Sorry. You can't make the perfect firework show.")

if fireworks:
    print(f"Firework Effects left: {', '.join(str(x) for x in fireworks)}")
if power:
    print(f"Explosive Power left: {', '.join(str(x) for x in power)}")

for key, value in collected.items():
    print(f"{key}: {value}")