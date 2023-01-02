budget = float(input())
season = input()

price = 0
vacation_place = ""
destination = ""

if budget <= 100:
    destination = "Bulgaria"
elif 100 < budget <= 1000:
    destination = "Balkans"
elif budget > 1000:
    destination = "Europe"

if destination == "Europe":
    vacation_place = "Hotel"
elif season == "summer":
    vacation_place = "Camp"
elif season == "winter":
    vacation_place = "Hotel"

if destination == "Bulgaria":
    if season == "summer":
        price = budget - (budget * 0.30)
    elif season == "winter":
        price = budget - (budget * 0.70)
elif destination == "Balkans":
    if season == "summer":
        price = budget - (budget * 0.40)
    elif season == "winter":
        price = budget - (budget * 0.80)
elif destination == "Europe":
    price = budget - (budget * 0.90)

money_left = budget - price

print(f"Somewhere in {destination}")
print(f"{vacation_place} - {money_left:.2f}")
