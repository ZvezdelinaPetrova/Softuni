from math import ceil

average_speed = float(input())
liters_per_kilometers = float(input())

distance = 384400 * 2
time_in_trip = ceil(distance / average_speed)
total_time = time_in_trip + 3
fuel = (liters_per_kilometers * distance) / 100

print(f"{total_time}")
print(f"{int(fuel)}")



