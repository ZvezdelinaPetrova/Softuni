prices_without_tax = input()

total_without_tax = 0
invalid_order = False
final_price = 0

while prices_without_tax != "regular" and prices_without_tax != "special":
    price_as_number = float(prices_without_tax)
    if price_as_number > 0:
        total_without_tax += price_as_number
    else:
        print("Invalid price!")
    prices_without_tax = input()

tax = total_without_tax * 0.20
final_price = tax + total_without_tax
if final_price == 0:
    print("Invalid order!")
    exit()
if prices_without_tax == "special":
    final_price -= final_price * 0.1
    if final_price == 0:
        print("Invalid order!")
        invalid_order = True
if not invalid_order:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_without_tax:.2f}$")
    print(f"Taxes: {tax:.2f}$")
    print("-----------")
    print(f"Total price: {final_price:.2f}$")
