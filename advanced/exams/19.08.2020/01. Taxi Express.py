from collections import deque


customers = deque(int(x) for x in input().split(", "))  # first
taxis = deque(int(x) for x in input().split(", "))  # last

total = 0

while customers and taxis:
    current_customer = customers.popleft()
    current_taxi = taxis.pop()
    if current_customer > current_taxi:
        customers.appendleft(current_customer)
    elif current_customer <= current_taxi:
        total += current_customer

if not customers:
    print(f"All customers were driven to their destinations")
    print(f"Total time: {total} minutes")
if not taxis and customers:
    print(f"Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join(str(x) for x in customers)}")

