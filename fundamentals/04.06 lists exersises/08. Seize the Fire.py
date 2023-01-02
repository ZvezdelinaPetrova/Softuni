fire_level = input().split("#")
amount_of_water = int(input())

total_fire = 0
effort = 0
new_list = []
for i in fire_level:
    current_fire = i.split()
    current_cell = current_fire[0]
    current_water = int(current_fire[2])
    if current_water > amount_of_water:
        continue
    if 81 <= current_water <= 125 and current_cell == "High":
        amount_of_water -= current_water
        total_fire += current_water
        effort += current_water * 0.25
        new_list.append(current_water)
    elif 51 <= current_water <= 80 and current_cell == "Medium":
        amount_of_water -= current_water
        total_fire += current_water
        effort += current_water * 0.25
        new_list.append(current_water)
    elif 1 <= current_water <= 50 and current_cell == "Low":
        amount_of_water -= current_water
        total_fire += current_water
        effort += current_water * 0.25
        new_list.append(current_water)

print("Cells:")
for g in new_list:
    print(f" - {g}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")