from collections import deque


pizzas = deque(int(x) for x in input().split(", "))   # first
workers = deque(int(x) for x in input().split(", "))   # last
total = 0

while pizzas and workers:
    current_pizza = pizzas.popleft()
    current_worker = workers.pop()
    if current_pizza <= 0:
        workers.append(current_worker)
        continue
    if current_pizza > 10:
        workers.append(current_worker)
        continue

    if current_pizza <= current_worker:
        total += current_pizza
    elif current_pizza > current_worker:
        if workers:
            pizzas.appendleft(current_pizza - current_worker)
            total += current_worker
        else:
            pizzas.appendleft(current_pizza - current_worker)


if not pizzas:
    print(f"All orders are successfully completed!")
    print(f"Total pizzas made: {total}")
    print(f"Employees: {', '.join(str(x) for x in workers)}")


if not workers and pizzas:
    print(f"Not all orders are completed.")
    print(f"Orders left: {', '.join(str(x) for x in pizzas)}")

