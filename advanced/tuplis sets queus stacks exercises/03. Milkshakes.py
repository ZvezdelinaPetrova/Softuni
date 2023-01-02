from collections import deque

chocolate = deque(int(x) for x in input().split(", "))  # last
milk = deque(int(x) for x in input().split(", "))  # first


milkshakes = 0

while milkshakes < 5 and chocolate and milk:
    current_chocolate = chocolate.pop()
    current_milk = milk.popleft()

    if current_milk <= 0 and current_chocolate <= 0:
        continue
    if current_chocolate <= 0:
        milk.appendleft(current_milk)
        continue
    if current_milk <= 0:
        chocolate.append(current_chocolate)
        continue

    elif current_chocolate == current_milk:
        milkshakes += 1
        continue
    else:
        milk.append(current_milk)
        chocolate.append(current_chocolate - 5)


if milkshakes >= 5:
    print(f"Great! You made all the chocolate milkshakes needed!")
else:
    print(f"Not enough milkshakes.")
if chocolate:
    print(f"Chocolate: {', '.join(str(x) for x in chocolate)}")
else:
    print(f"Chocolate: empty")
if milk:
    print(f"Milk: {', '.join(str(x) for x in milk)}")
else:
    print(f"Milk: empty")