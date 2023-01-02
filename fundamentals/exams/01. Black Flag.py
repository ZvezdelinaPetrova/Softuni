days = int(input())
plunder_per_day = int(input())
expected_plunder = float(input())

current_plunder = 0

for i in range(1, days + 1):
    current_plunder += plunder_per_day
    if i % 3 == 0:
        current_plunder += plunder_per_day * 0.5
    if i % 5 == 0:
        current_plunder -= current_plunder * 0.3
if current_plunder >= expected_plunder:
    print(f"Ahoy! {current_plunder:.2f} plunder gained.")
else:
    left = expected_plunder - current_plunder
    percentage_left = (left * 100) / expected_plunder
    percentage = 100 - percentage_left
    print(f"Collected only {percentage:.2f}% of the plunder.")