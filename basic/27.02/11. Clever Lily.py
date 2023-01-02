age = int(input())
price_of_laundry = float(input())
price_per_toy = int(input())
toys = 0
money = 0
total_toys_money = 0

for i in range(1, age + 1):
    if i % 2 == 1:
        toys = toys + 1
    elif i % 2 == 0:
        money = money + (i * 10 / 2)
for i in range(1, age + 1):
    if i % 2 == 0:
        money = money - 1
    elif i % 2 == 1:
        total_toys_money = toys * price_per_toy

money = money + total_toys_money

if price_of_laundry <= money:
    print(f"Yes! {money - price_of_laundry:.2f}")
elif money < price_of_laundry:
    print(f"No! {price_of_laundry - money:.2f}")

