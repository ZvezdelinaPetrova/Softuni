def shopping_cart(*args):
    # collected = {
    #     "Soup": 3,
    #     "Pizza": 4,
    #     "Dessert": 2
    # }
    new_dict = {
        "Soup": [],
        "Pizza": [],
        "Dessert": []
    }
    for x in args:
        if x == "Stop":
            if len(new_dict["Soup"]) == 0 and len(new_dict["Pizza"]) == 0 and len(new_dict["Dessert"]) == 0:
                return f"No products in the cart!"
            else:
                test = sorted(new_dict.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
                result = ""
                for key, value in test:
                    result += f"{key}:" + "\n"
                    for el in sorted(value):
                        result += f" - {el}" + "\n"
                return result
        else:
            meal, product = x[0], x[1]
            if meal not in new_dict:
                new_dict[meal] = []
                new_dict[meal].append(product)
            else:
                if product in new_dict[meal]:
                    continue
                else:
                    if meal == "Soup":
                        if len(new_dict[meal]) >= 3:
                            continue
                        else:
                            new_dict[meal].append(product)
                    elif meal == "Pizza":
                        if len(new_dict[meal]) >= 4:
                            continue
                        else:
                            new_dict[meal].append(product)
                    elif meal == "Dessert":
                        if len(new_dict[meal]) >= 2:
                            continue
                        else:
                            new_dict[meal].append(product)

    test = sorted(new_dict.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
    result = ""
    for key, value in test:
        result += f"{key}:" + "\n"
        for el in sorted(value):
            result += f" - {el}" + "\n"

    return result.strip()

# print(shopping_cart(
#     ('Pizza', 'ham'),
#     ('Soup', 'carrots'),
#     ('Pizza', 'cheese'),
#     ('Pizza', 'flour'),
#     ('Dessert', 'milk'),
#     ('Pizza', 'mushrooms'),
#     ('Pizza', 'tomatoes'),
#     'Stop',
# ))

# print(shopping_cart(
#     ('Pizza', 'ham'),
#     ('Dessert', 'milk'),
#     ('Pizza', 'ham'),
#     'Stop',
# ))
print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))
