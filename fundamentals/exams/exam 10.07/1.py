how_many_orders = int(input())

current_price = 0

for i in range(1, how_many_orders + 1):
    price_per_capsule = float(input())
    days = int(input())
    capsule_count = int(input())
    price = (days * capsule_count) * price_per_capsule
    print(f"The price for the coffee is: ${price:.2f}")
    current_price += price

total = current_price

print(f"Total: ${total:.2f}")