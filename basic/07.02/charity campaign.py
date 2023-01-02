number_of_days = int(input())
number_of_people = int(input())
number_of_cakes = int(input())
number_of_waffles = int(input())
number_of_pancakes = int(input())
cake_price = number_of_cakes * 45
waffles_price = number_of_waffles * 5.80
pancakes_price = number_of_pancakes * 3.2
price_per_day = (cake_price + waffles_price + pancakes_price) * number_of_people
sum_of_the_company = price_per_day * number_of_days
sum_all = sum_of_the_company - sum_of_the_company * 1/8
print(sum_all)





