items = input().split("|")
budget = float(input())

profit = 0
list_items = []
all_p = 0
for i in items:
    current_item = i.split("->")
    current_type = current_item[0]
    current_price = float(current_item[1])
    if current_price > budget:
        continue
    if current_type == "Clothes" and current_price <= 50.00:
        budget -= current_price
        profit += current_price * 0.40
        new_price = current_price + current_price * 0.40
        list_items.append(new_price)
    elif current_type == "Shoes" and current_price <= 35.00:
        budget -= current_price
        profit += current_price * 0.40
        new_price = current_price + current_price * 0.40
        list_items.append(new_price)
    elif current_type == "Accessories" and current_price <= 20.50:
        budget -= current_price
        profit += current_price * 0.40
        new_price = current_price + current_price * 0.40
        list_items.append(new_price)

for g in list_items:
    price = g
    all_p += price
    print(f"{g:.2f} ", end="")
print()
print(f"Profit: {profit:.2f}")

final_amount = budget + all_p

if final_amount >= 150:
    print("Hello, France!")
else:
    print("Time to go.")
