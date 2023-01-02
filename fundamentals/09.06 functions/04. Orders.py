def calculate_price(item_name, count):
    if item_name == "coffee":
        return 1.50 * count
    elif item_name == "coke":
        return 1.40 * count
    elif item_name == "water":
        return 1 * count
    elif item_name == "snacks":
        return 2 * count


product_name = input()
price_per_product = float(input())

formatted = calculate_price(product_name, price_per_product)

print(f"{formatted:.2f}")