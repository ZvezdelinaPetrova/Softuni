from collections import deque


eggs = deque(int(x) for x in input().split(", "))  # first
numbers = deque(int(x) for x in input().split(", "))  # last

collected = 0

while eggs and numbers:
    current_egg = eggs.popleft()
    current_number = numbers.pop()
    if current_egg <= 0:
        numbers.append(current_number)
        continue
    if current_egg == 13:
        numbers.append(numbers.popleft())
        numbers.appendleft(current_number)
        continue
    result = current_egg + current_number
    if result <= 50:
        collected += 1


if collected > 0:
    print(f"Great! You filled {collected} boxes.")
else:
    print(f"Sorry! You couldn't fill any boxes!")
if eggs:
    print(f"Eggs left: {', '.join(str(x) for x in eggs)}")

if numbers:
    print(f"Pieces of paper left: {', '.join(str(x) for x in numbers)}")


