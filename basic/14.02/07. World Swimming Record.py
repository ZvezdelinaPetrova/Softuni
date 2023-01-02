from math import floor
record_in_seconds = float(input())
distance_in_meters = float(input())
swim_time_for_one_meter = float(input())

how_long = swim_time_for_one_meter * distance_in_meters

lateness = distance_in_meters / 15
lateness_in_seconds = floor(lateness) * 12.5
total_time = how_long + lateness_in_seconds

if record_in_seconds > total_time:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
elif record_in_seconds <= total_time:
    ivan_time = total_time - record_in_seconds
    print(f"No, he failed! He was {ivan_time:.2f} seconds slower.")
