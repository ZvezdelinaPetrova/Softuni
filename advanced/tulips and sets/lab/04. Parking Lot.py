n = int(input())

new_set = []

for _ in range(n):
    data = input().split(", ")
    action = data[0]
    number = data[1]
    if action == "IN":
        new_set.append(number)
    elif action == "OUT":
        new_set.remove(number)

new_set = set(new_set)

if new_set:
    for i in new_set:
        print(i)
else:
    print("Parking Lot is Empty")

# moje da se napravi gore seta kato se sazdade taka
# new_set = set() i v ngo veche da se izpolzvat .add i .remove

#
# number = int(input())
#
# cars_list = []
#
# for x in range(number):
#     current_car = input().split(", ")
#     action = current_car[0]
#     car_number = current_car[1]
#     if action == "IN":
#         if car_number in cars_list:
#             continue
#         else:
#             cars_list.append(car_number)
#     elif action == "OUT":
#         if car_number in cars_list:
#             cars_list.remove(car_number)
#
# if cars_list:
#     for car in cars_list:
#         print(f"{car}")
# else:
#     print(f"Parking Lot is Empty")