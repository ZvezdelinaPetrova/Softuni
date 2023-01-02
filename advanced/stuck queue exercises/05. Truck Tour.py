from collections import deque

pumps = int(input())
queue = deque()


for i in range(pumps):
    data = input().split()
    current_liters = int(data[0])
    current_kilometers = int(data[1])
    queue.append([current_liters, current_kilometers])


for i in range(pumps):
    circles = 0
    counter = 0
    for item in queue:
        liters = item[0]
        kilometers = item[1]
        counter += liters
        if counter < kilometers:
            break
        counter -= kilometers
        circles += 1
    if circles == len(queue):
        print(i)
        break

    queue.rotate(-1)

