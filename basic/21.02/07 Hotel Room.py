month = input()
nights = int(input())

price_studio = 0
price_apartment = 0

if month == "May" or month == "October":
    price_studio = 50 * nights
    price_apartment = 65 * nights
elif month == "June" or month == "September":
    price_studio = 75.20 * nights
    price_apartment = 68.70 * nights
elif month == "July" or month == "August":
    price_studio = 76 * nights
    price_apartment = 77 * nights

if month == "May" or month == "October":
    if nights > 14:
        price_studio -= price_studio * 0.30
        price_apartment -= price_apartment * 0.10
if month == "May" or month == "October":
    if 14 >= nights > 7:
        price_studio -= price_studio * 0.05
if month == "June" or month == "September":
    if nights > 14:
        price_studio -= price_studio * 0.20
        price_apartment -= price_apartment * 0.10
if month == "July" or month == "August":
    if nights > 14:
        price_apartment -= price_apartment * 0.10
print(f"Apartment: {price_apartment:.2f} lv.")

print(f"Studio: {price_studio:.2f} lv.")





