persons = int(input())
capacity = int(input())

courses = 0
course = persons // capacity
reminder = persons % capacity

if course == 0:
    course += 1
    print(course)
elif reminder > 0:
    course += 1
    print(course)
elif reminder == 0:
    print(course)


