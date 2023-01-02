money = float(input())
total = int(money * 100)
coins = 0

two = 0
one = 0
fifty_cent = 0
twenty_cent = 0
ten_cent = 0
five_cent = 0
two_cent = 0
one_cent = 0

while total > 0:
    if total // 200 > 0:
        two = total // 200
        if two >= 1:
            coins += two
            total -= two * 200
    if total // 100 > 0:
        one = total // 100
        if one >= 1:
            coins += one
            total -= one * 100
    if total // 50 > 0:
        fifty_cent = total // 50
        if fifty_cent >= 1:
            coins += fifty_cent
            total -= fifty_cent * 50
    if total // 20 > 0:
        twenty_cent = total // 20
        if twenty_cent >= 1:
            coins += twenty_cent
            total -= twenty_cent * 20
    if total // 10 > 0:
        ten_cent = total // 10
        if ten_cent >= 1:
            coins += ten_cent
            total -= ten_cent * 10
    if total // 5 > 0:
        five_cent = total // 5
        if five_cent >= 1:
            coins += five_cent
            total -= five_cent * 5
    if total // 2 > 0:
        two_cent = total // 2
        if two_cent >= 1:
            coins += two_cent
            total -= two_cent * 2
    if total // 1 > 0:
        one_cent = total // 1
        if one_cent == 1:
            coins += one_cent
            total -= one_cent * 1
print(coins)