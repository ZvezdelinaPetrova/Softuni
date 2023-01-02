employee_1 = int(input())
employee_2 = int(input())
employee_3 = int(input())
students = int(input())

max_per_hour = employee_1 + employee_2 + employee_3
hours = 0

while students > 0:
    hours += 1
    students -= max_per_hour
    if hours % 4 == 0:
        hours += 1

print(f"Time needed: {hours}h.")