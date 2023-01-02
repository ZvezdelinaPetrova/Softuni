command = input()

products_dict = {}

while command != "buy":
    name, price, quantity = command.split()
    price = float(price)
    quantity = int(quantity)
    if name not in products_dict:
        products_dict[name] = {"price": price, "quantity": quantity}
    elif name in products_dict:
        if products_dict[name] != price:
            products_dict[name]["price"] = price
        products_dict[name]["quantity"] += quantity
    command = input()

for key, value in products_dict.items():
    total_price = products_dict[key]["price"] * products_dict[key]["quantity"]
    print(f"{key} -> {total_price:.2f}")