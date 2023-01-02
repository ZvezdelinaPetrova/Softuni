from collections import deque

quantity = int(input())

orders = deque([int(x) for x in input().split()])

print(max(orders))

while orders:
    current_order = orders[0]
    if current_order <= quantity:
        quantity -= current_order
        orders.popleft()
        if quantity == 0:
            break
    else:
        break

if not orders:
    print("Orders complete")
else:
    print(f"Orders left: {' '.join(str(x) for x in orders)}")


#
# from collections import deque
# food_amount = int(input())
# orders = [int(i) for i in input().split()]
#
# queue = deque(orders)
# print(max(queue))
#
# while queue:
#     first_in_the_queue = queue[0]
#     if first_in_the_queue > food_amount:
#         queue = [str(i) for i in queue]
#         print(f"Orders left: {' '.join(queue)}")
#         break
#     else:
#         food_amount -= first_in_the_queue
#         queue.popleft()
#
# if len(queue) <= 0:
#     print(f"Orders complete")