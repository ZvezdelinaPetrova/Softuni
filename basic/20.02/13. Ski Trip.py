days = int(input())
room_type = input()
opinion = input()

nights = days - 1
price_per_night = 0

if room_type == "room for one person":
    price_per_night = 18
elif room_type == "apartment":
    price_per_night = 25
elif room_type == "president apartment":
    price_per_night = 35

total_price = price_per_night * nights

if room_type == "room for one person":
    if days < 10:
        total_price = total_price
    elif 10 <= days <= 15:
        total_price = total_price
    elif days > 15:
        total_price = total_price
elif room_type == "apartment":
    if days < 10:
        total_price = total_price - total_price * 0.30
    elif 10 <= days <= 15:
        total_price = total_price - total_price * 0.35
    elif days > 15:
        total_price = total_price - total_price * 0.50
elif room_type == "president apartment":
    if days < 10:
        total_price = total_price - total_price * 0.10
    elif 10 <= days <= 15:
        total_price = total_price - total_price * 0.15
    elif days > 15:
        total_price = total_price - total_price * 0.20

if opinion == "positive":
    total_price = total_price + total_price * 0.25
elif opinion == "negative":
    total_price = total_price - total_price * 0.10

print(f"{total_price:.2f}")



