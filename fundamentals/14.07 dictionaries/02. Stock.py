products = input().split()
searched_products = input().split()

products_dict = {}

for i in range(0, len(products), 2):
    key = products[i]
    value = int(products[i + 1])
    products_dict[key] = value

for j in searched_products:
    if j in products_dict:
        print(f"We have {products_dict[j]} of {j} left")
    else:
        print(f"Sorry, we don't have {j}")