person_1 = int(input())
person_2 = int(input())
person_3 = int(input())
people = int(input())

max_per_hour = person_1 + person_2 + person_3
hours = 0

while people > 0:
    hours += 1
    people -= max_per_hour
    if hours % 4 == 0:
        hours += 1

print(f"Time needed: {hours}h.")