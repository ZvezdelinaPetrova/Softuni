from collections import deque

cups = deque([int(x) for x in input().split()]) # first cup
bottles = deque([int(x) for x in input().split()]) # from last

waisted = 0
while cups and bottles:
    current_cup = cups[0]
    current_bottle = bottles.pop()
    if current_bottle >= current_cup:
        cups.popleft()
        current_bottle -= current_cup
        if current_bottle > 0:
            waisted += current_bottle
    elif current_bottle < current_cup:
        current_cup -= current_bottle
        while current_cup > 0:
            if bottles:
                next_bottle = bottles.pop()
                if next_bottle >= current_cup:
                    result = next_bottle - current_cup
                    cups.popleft()
                    waisted += result
                    break
                else:
                    current_cup -= next_bottle
if not cups:
    print(f"Bottles: {' '.join(str(x) for x in reversed(bottles))}")
if not bottles:
    print(f"Cups: {' '.join(str(x) for x in cups)}")

print(f"Wasted litters of water: {waisted}")