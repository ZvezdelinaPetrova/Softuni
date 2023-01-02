from collections import deque

water = int(input())
people = deque()

command = input()

while command != "Start":
    people.append(command)
    command = input()

new_command = input()

while new_command != "End":
    what_to_do = new_command.split()
    if what_to_do[0] == "refill":
        water += int(what_to_do[1])
    else:
        amount = int(what_to_do[0])
        current_person = people.popleft()
        if amount <= water:
            water -= amount
            print(f"{current_person} got water")
        else:
            print(f"{current_person} must wait")
    new_command = input()

print(f"{water} liters left")



# from collections import deque
# litres_of_water = int(input())
#
# queue = deque()
#
# command = input()
#
# while command != "Start":
#     queue.append(command)
#     command = input()
#
# second_command = input()
#
# while second_command != "End":
#     action = second_command.split()
#     if action[0] == "refill":
#         liters_to_refill = int(action[1])
#         litres_of_water += liters_to_refill
#     else:
#         liters_to_drink = int(action[0])
#         if litres_of_water >= liters_to_drink:
#             litres_of_water -= liters_to_drink
#             person_to_delete = queue.popleft()
#             print(f"{person_to_delete} got water")
#         else:
#             person_to_delete = queue.popleft()
#             print(f"{person_to_delete} must wait")
#     second_command = input()
#
# print(f"{litres_of_water} liters left")

