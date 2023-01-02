strawberries_price = float(input())
banana_quantity = float(input())
orange_quantity = float(input())
raspberry_quantity = float(input())
strawberries_quantity = float(input())
raspberry_price = strawberries_price / 2
orange_price = raspberry_price * 0.6
banana_price = raspberry_price * 0.2
total_money = (strawberries_price * strawberries_quantity) + (raspberry_price * raspberry_quantity)\
              + (orange_price * orange_quantity) + (banana_price * banana_quantity)
print(total_money)



