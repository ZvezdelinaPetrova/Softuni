persons = int(input())
days = int(input())

counter_coins = 0
persons_all = persons

for i in range(1, days + 1):
    counter_coins += 50
    if i % 10 == 0:
        persons_all -= 2
    if i % 15 == 0:
        persons_all += 5

    counter_coins -= persons_all * 2
    if i % 3 == 0:
        counter_coins -= persons_all * 3
    if i % 5 == 0:
        counter_coins += persons_all * 20
        if i % 3 == 0:
            counter_coins -= persons_all * 2

coins_per_person = int(counter_coins / persons_all)
print(f"{persons_all} companions received {coins_per_person} coins each.")
