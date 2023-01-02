name = input()
total = 0
grade = 0
excluded = 0
while grade < 12:
    evaluation = float(input())
    total += evaluation
    if evaluation >= 4:
        grade = grade + 1
    if evaluation < 4:
        excluded += 1
    if excluded >= 2:
        grade += 1
        break
if grade >= 12:
    average_grade = total / grade
    print(f"{name} graduated. Average grade: {average_grade:.2f}")
elif grade < 12:
    print(f"{name} has been excluded at {grade} grade")
