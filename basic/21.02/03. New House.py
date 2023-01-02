flowers = input()
count_of_flowers = int(input())
budget = int(input())

price = 0
total_price = 0

if flowers == "Roses":
    price = 5
elif flowers == "Dahlias":
    price = 3.8
elif flowers == "Tulips":
    price = 2.8
elif flowers == "Narcissus":
    price = 3.0
elif flowers == "Gladiolus":
    price = 2.5

total_price = price * count_of_flowers

if count_of_flowers > 80 and flowers == "Roses":
    total_price -= total_price * 0.10
elif count_of_flowers > 90 and flowers == "Dahlias":
    total_price -= total_price * 0.15
elif count_of_flowers > 80 and flowers == "Tulips":
    total_price -= total_price * 0.15
elif count_of_flowers < 120 and flowers == "Narcissus":
    total_price += total_price * 0.15
elif count_of_flowers < 80 and flowers == "Gladiolus":
    total_price += total_price * 0.20

money_needed = budget - total_price

if total_price <= budget:
    print(f"Hey, you have a great garden with {count_of_flowers} {flowers} and {money_needed:.2f} leva left.")
elif total_price > budget:
    print(f"Not enough money, you need {-money_needed:.2f} leva more.")


