from collections import deque

green = int(input())
additional_time = int(input())

cars = deque()

data = input()
total = 0
green_all = green
crashed = False
letter = ''
while data != "END":
    if data != "green":
        cars.append(data)
    elif data == "green":
        green_all = green
        while cars:
            car = cars.popleft()
            len_of_car = len(car)
            if len_of_car <= green_all:
                total += 1
                green_all -= len_of_car
                if green_all == 0:
                    break
            else:
                if len_of_car <= green_all + additional_time:
                    total += 1
                    break
                else:
                    char_to_hit = green_all + additional_time
                    letter = car[char_to_hit]
                    crashed = True
                    print("A crash happened!")
                    print(f"{car} was hit at {letter}.")
                    exit()
    data = input()

if not crashed:
    print("Everyone is safe.")
    print(f"{total} total cars passed the crossroads.")


# from collections import deque
#
# duration_of_green = int(input())
# duration_of_free_window = int(input())
#
#
# cars = deque()
# crash = False
#
# total_cars_passed_count = 0
#
# command = input()
# while command != "END":
#     green_counter = duration_of_green
#     if command == "green":
#         while cars:
#             current_car = cars.popleft()
#             if len(current_car) < green_counter:
#                 green_counter -= len(current_car)
#                 total_cars_passed_count += 1
#                 continue
#             elif len(current_car) == green_counter:
#                 total_cars_passed_count += 1
#                 break
#             elif len(current_car) > green_counter:
#                 if green_counter + duration_of_free_window >= len(current_car):
#                     total_cars_passed_count += 1
#                     break
#                 else:
#                     total = green_counter + duration_of_free_window
#                     letter_to_hit = current_car[total]
#                     crash = True
#                     print(f"A crash happened!")
#                     print(f"{current_car} was hit at {letter_to_hit}.")
#                     exit()
#     else:
#         cars.append(command)
#     command = input()
#
#
# if not crash:
#     print(f"Everyone is safe.")
#     print(f"{total_cars_passed_count} total cars passed the crossroads.")
