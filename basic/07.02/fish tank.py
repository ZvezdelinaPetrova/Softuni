length_cm = int(input())
wide_cm = int(input())
height_cm = int(input())
volume_percentage = float(input())
aquarium_capacity = length_cm * wide_cm * height_cm
liters_to_take = aquarium_capacity * 0.001
percentage = volume_percentage * 0.01
total_needed = liters_to_take * (1-percentage)
print(total_needed)


