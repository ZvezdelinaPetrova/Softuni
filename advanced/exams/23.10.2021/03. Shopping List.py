def shopping_list(budget, **kwargs):
    text_to_print = ""
    if budget < 100:
        return f"You do not have enough budget."
    basket = 5
    for key, value in kwargs.items():
        price, quantity = value[0], value[1]
        result = price * quantity
        if budget >= result:
            budget -= result
            text_to_print += f"You bought {key} for {result:.2f} leva." + "\n"
            basket -= 1
            if basket == 0:
                break
    return text_to_print.strip()


print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))




