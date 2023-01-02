money = float(input())
total = int(money * 100)
coins = 0
counter = 0

while total > 0:
    if total >= 200:
        coins = total // 200
        total -= coins * 200
        counter += coins
    elif total >= 100:
        coins = total // 100
        total -= coins * 100
        counter += coins
    elif total >= 50:
        coins = total // 50
        total -= coins * 50
        counter += coins
    elif total >= 20:
        coins = total // 20
        total -= coins * 20
        counter += coins
    elif total >= 10:
        coins = total // 10
        total -= coins * 10
        counter += coins
    elif total >= 5:
        coins = total // 5
        total -= coins * 5
        counter += coins
    elif total >= 2:
        coins = total // 2
        total -= coins * 2
        counter += coins
    elif total == 1:
        coins = total // 1
        total -= coins * 1
        counter += coins

print(counter)
