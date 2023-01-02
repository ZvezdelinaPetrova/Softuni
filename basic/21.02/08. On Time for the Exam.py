hour_of_exam = int(input())
minutes_of_exam = int(input())
hour_of_arrival = int(input())
minutes_of_arrival = int(input())

time_of_arrival = hour_of_arrival * 60 + minutes_of_arrival
time_of_exam = hour_of_exam * 60 + minutes_of_exam

if time_of_arrival > time_of_exam:
    print("Late")
elif time_of_exam - 30 <= time_of_arrival <= time_of_exam:
    print("On Time")
else:
    print("Early")


if time_of_exam - 60 < time_of_arrival < time_of_exam:
    time_of_arrival = time_of_exam - time_of_arrival
    print(f"{time_of_arrival} minutes before the start")
elif time_of_exam + 60 > time_of_arrival > time_of_exam:
    time_of_arrival = time_of_arrival - time_of_exam
    print(f"{time_of_arrival} minutes after the start")
elif time_of_exam - 60 >= time_of_arrival:
    difference = time_of_exam - time_of_arrival
    hours = difference // 60
    minutes = difference % 60
    print(f"{hours}:{minutes:0>2d} hours before the start")
elif time_of_exam + 60 <= time_of_arrival:
    difference = time_of_arrival - time_of_exam
    hours = difference // 60
    minutes = difference % 60
    print(f"{hours}:{minutes:0>2d} hours after the start")


