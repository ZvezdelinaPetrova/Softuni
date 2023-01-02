from collections import deque


bowls = deque(int(x) for x in input().split(", "))  # last
customers = deque(int(x) for x in input().split(", "))  # first


while bowls and customers:
    current_bowl = bowls.pop()
    current_customer = customers.popleft()
    if current_customer == current_bowl:
        continue
    elif current_bowl > current_customer:
        bowls.append(current_bowl - current_customer)

    elif current_bowl < current_customer:
        customers.appendleft(current_customer - current_bowl)


if not customers:
    print(f"Great job! You served all the customers.")
    if bowls:
        print(f"Bowls of ramen left: {', '.join(str(x) for x in bowls)}")
else:
    print(f"Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(str(x) for x in customers)}")
