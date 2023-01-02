from math import ceil
import sys

students_count = int(input())
lectures_count = int(input())
initial_bonus = int(input())

max_bonus = 0
most_attended = 0

for i in range(students_count):
    attendance = int(input())
    bonus = attendance / lectures_count * (5 + initial_bonus)
    if bonus > max_bonus:
        max_bonus = bonus
        most_attended = attendance
print(f"Max Bonus: {ceil(max_bonus)}.")
print(f"The student has attended {most_attended} lectures.")

