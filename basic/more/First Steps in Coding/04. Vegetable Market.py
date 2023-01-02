price_for_vegetables = float(input())
price_for_fruits = float(input())
how_many_vegetables = int(input())
how_many_fruits = int(input())

total_price_vegetables = price_for_vegetables * how_many_vegetables
total_price_fruits = price_for_fruits * how_many_fruits

sum_for_all = (total_price_fruits + total_price_vegetables) / 1.94
print(f"{sum_for_all:.2f}")