from collections import deque

children = [x for x in input().split()]
number = int(input())
children_deque = deque(children)

counter = 1

while len(children_deque) != 1:
    current_kid = children_deque.popleft()
    if counter == number:
        counter = 1
        print(f"Removed {current_kid}")
    else:
        children_deque.append(current_kid)
        counter += 1

print(f"Last is {children_deque[0]}")



# from collections import deque
#
# kids = input().split()
# which_number = int(input())
# queue = deque(kids)
# counter = 1
# while len(queue) != 1:
#     for i in range(which_number - 1):
#         name_to_append = queue.popleft()
#         queue.append(name_to_append)
#     name_to_delete = queue.popleft()
#     print(f"Removed {name_to_delete}")
#
# print(f"Last is {''.join(queue)}")

