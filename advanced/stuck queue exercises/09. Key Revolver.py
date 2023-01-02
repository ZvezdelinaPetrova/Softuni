from collections import deque

price_of_bullet = int(input())
size_of_gun_barrel = int(input())
bullets = [int(x) for x in input().split()]  # отзад апред
locks = deque([int(x) for x in input().split()])  # отпред назад
intelligence = int(input())

shot_count = 0
barrel_counter = size_of_gun_barrel
while bullets and locks:

    current_bullet = bullets.pop()
    current_lock = locks[0]
    shot_count += 1

    if current_bullet <= current_lock:
        locks.popleft()
        print(f"Bang!")
    else:
        print(f"Ping!")
    barrel_counter -= 1
    if barrel_counter == 0:
        if bullets:
            print(f"Reloading!")
        barrel_counter = size_of_gun_barrel


bullet_cost = shot_count * price_of_bullet
money_earned = intelligence - bullet_cost

if not locks:
    print(f"{len(bullets)} bullets left. Earned ${money_earned}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")