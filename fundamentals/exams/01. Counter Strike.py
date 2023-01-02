energy = int(input())

command = input()
counter = 0
died = False

while command != "End of battle":
    distance = int(command)
    if energy < distance:
        died = True
        print(f"Not enough energy! Game ends with {counter} won battles and {energy} energy")
        break
    elif energy >= distance:
        energy -= distance
        counter += 1
        if counter % 3 == 0:
            energy += counter
    command = input()

if not died:
    print(f"Won battles: {counter}. Energy left: {energy}")