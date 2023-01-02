command = input()

products = {}

while command != "statistics":
    key, quantity = command.split(": ")
    if key not in products:
        products[key] = int(quantity)
    elif key in products:
        products[key] += int(quantity)

    command = input()

print(f"Products in stock:")
for key, quantity in products.items():
    print(f"- {key}: {quantity}")

print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")