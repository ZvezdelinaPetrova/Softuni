from math import floor

width = float(input())
length = float(input())
height = float(input())
people_height = float(input())

area_of_ship = width * length * height
area_per_room = (people_height + 0.40) * 2 * 2
how_many_people = floor(area_of_ship / area_per_room)

if 3 <= how_many_people <= 10:
    print(f"The spacecraft holds {how_many_people} astronauts.")
elif how_many_people < 3:
    print("The spacecraft is too small.")
elif how_many_people > 10:
    print("The spacecraft is too big.")

