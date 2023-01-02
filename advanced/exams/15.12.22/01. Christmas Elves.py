from collections import deque


elfs = deque([int(i) for i in input().split()]) # first
materials = [int(i) for i in input().split()]  # last
total_toys = 0
total_energy = 0
counter = 0
while elfs and materials:
    current_elf = elfs.popleft()
    current_material = materials.pop()
    if current_elf < 5:
        materials.append(current_material)
        continue
    counter += 1
    if current_elf >= current_material:
        if counter % 3 == 0:
            if current_elf >= current_material * 2:
                total_toys += 2
                total_energy += current_material * 2
                elfs.append(current_elf - (current_material * 2) + 1)
                if counter % 5 == 0:
                    total_toys -= 2
                    elfs[-1] -= 1
            else:
                elfs.append(current_elf * 2)
                materials.append(current_material)

        elif counter % 5 == 0:
            elfs.append(current_elf - current_material)
            total_energy += current_material
        else:
            total_toys += 1
            total_energy += current_material
            elfs.append(current_elf - current_material + 1)

    elif current_elf < current_material:
        materials.append(current_material)
        elfs.append(current_elf * 2)


print(f"Toys: {total_toys}")
print(f"Energy: {total_energy}")


if elfs:
    print(f"Elves left: {', '.join(str(x) for x in elfs)}")

if materials:
    print(f"Boxes left: {', '.join(str(x) for x in materials)}")
