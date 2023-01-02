from collections import deque


def flights(*args):
    new_dict = {}
    new_info = deque(args)
    current_element = new_info.popleft()
    while current_element != "Finish":
        if current_element not in new_dict:
            next_element = new_info.popleft()
            new_dict[current_element] = int(next_element)
        else:
            next_element = new_info.popleft()
            new_dict[current_element] += int(next_element)
        current_element = new_info.popleft()
    return new_dict


# def flights(*args):
#     new_dict = {}
#     new_list = []
#     for i in args:
#         if i == "Finish":
#             break
#         else:
#             new_list.append(i)
#
#     for j in range(0, len(new_list), 2):
#         current_el = new_list[j]
#         value = int(new_list[j + 1])
#         if current_el in new_dict:
#             new_dict[current_el] += value
#         else:
#             new_dict[current_el] = value
#
#     return new_dict


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))