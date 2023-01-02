from collections import deque


def best_list_pureness(new_list, number):
    l = deque(new_list)
    results = []
    for x in range(number + 1):
        current_sum = 0
        for y in range(len(l)):
            current_sum += y * l[y]
        results.append(current_sum)
        l.rotate(1)
    max_el = max(results)
    rotation = results.index(max_el)
    return f"Best pureness {max_el} after {rotation} rotations"


# from collections import deque
#
#
# def best_list_pureness(numbers, k):
#     data = {}
#     numbers = deque(numbers)
#
#     for rotation in range(k+1):
#         result = sum([index * number for index, number in enumerate(numbers)])
#         data.update({rotation: result})
#         numbers.appendleft(numbers.pop())
#     max_pureness = max(data.values())
#     for key, val in data.items():
#         if max_pureness == val:
#             return f'Best pureness {val} after {key} rotations'


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)