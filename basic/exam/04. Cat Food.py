cats = int(input())

group_1_count = 0
group_2_count = 0
group_3_count = 0
total_counter = 0

for i in range(cats):
    food = float(input())
    if 100 <= food < 200:
        group_1_count += 1
        total_counter += food
    elif 200 <= food < 300:
        group_2_count += 1
        total_counter += food
    elif 300 <= food < 400:
        group_3_count += 1
        total_counter += food

price = (total_counter / 1000) * 12.45

print(f"Group 1: {group_1_count} cats.")
print(f"Group 2: {group_2_count} cats.")
print(f"fGroup 3: {group_3_count} cats.")
print(f"Price for food per day: {price:.2f} lv.")
