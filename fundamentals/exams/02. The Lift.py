# people = int(input())
# wagons = [int(el) for el in input().split()]
#
# counter = 0
#
# for i in range(len(wagons)):
#     if wagons[i] == 0:
#         if people >= 4:
#             wagons[i] = 4
#             people -= 4
#         elif people < 4:
#             wagons[i] = people
#             people = 0
#     elif wagons[i] == 1:
#         if people >= 3:
#             wagons[i] = 4
#             people -= 3
#         elif 0 < people < 3:
#             wagons[i] = 1 + people
#     elif wagons[i] == 2:
#         if people >= 2:
#             wagons[i] = 4
#             people -= 2
#         elif 0 < people < 2:
#             wagons[i] = 3
#             people -= 1
#     elif wagons[i] == 3:
#         if people >= 1:
#             wagons[i] = 4
#             people -= 1
#     elif wagons[i] == 4:
#         if people >= 1:
#             continue
#
# for j in wagons:
#     if j == 4:
#         continue
#     elif j < 4:
#         counter += 1
#
# if people == 0 and counter >= 1:
#     print(f"The lift has empty spots!")
#     print(*wagons, sep=" ")
# elif people >= 1 and counter == 0:
#     print(f"There isn't enough space! {people} people in a queue!")
#     print(*wagons, sep=" ")
# elif people == 0 and counter == 0:
#     print(*wagons, sep=" ")

people = int(input())
train = input().split()
wagons = [int(wagon) for wagon in train]


for i in range(len(wagons)):
    if wagons[i] < 4:
        a = 4 - wagons[i]
        if people >= a:
            people -= a
            wagons[i] += a
        else:
            wagons[i] += people
            people = 0

wagons_list = [str(wagon) for wagon in wagons]

if people == 0:
    if wagons.count(4) == len(wagons):
        print(' '.join(wagons_list))
    elif wagons.count(4) < len(wagons):
        print(f"The lift has empty spots!")
        print(' '.join(wagons_list))
else:
    print(f"There isn't enough space! {people} people in a queue!")
    print(' '.join(wagons_list))