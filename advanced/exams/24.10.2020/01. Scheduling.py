from collections import deque

numbers = deque(int(x) for x in input().split(", "))
index = int(input())
rotate_number = index
searched_item = numbers[index]
numbers.rotate(-rotate_number)
result = sum(x for x in numbers if x <= searched_item)
print(result)


# from collections import deque
#
# tasks = [int(el) for el in input().split(', ')]
# searched_index = int(input())
# result = 0
#
# cycles = deque(sorted([(tasks[index], index)for index in range(len(tasks))]))
#
# while cycles:
#     number, index = cycles.popleft()
#     result += number
#     if index == searched_index:
#         print(result)
#         break