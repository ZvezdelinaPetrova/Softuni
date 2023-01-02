movie_budget = float(input())
people = int(input())
people_dress_price = float(input())

decoration = movie_budget * 0.1


if people > 150:
    dress_all = people * (people_dress_price - people_dress_price * 0.1)
elif people <= 150:
    dress_all = people * people_dress_price

money_all = decoration + dress_all

if movie_budget < money_all:
    left_money = money_all - movie_budget
    print("Not enough money!")
    print(f"Wingard needs {left_money:.2f} leva more.")
elif movie_budget >= money_all:
    money_plus = movie_budget - money_all
    print("Action!")
    print(f"Wingard starts filming with {money_plus:.2f} leva left.")
