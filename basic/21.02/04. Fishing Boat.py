budget = int(input())
season = input()
count_of_people = int(input())

# proverka za sezona i cenata
# proverka za cenata s otstapka spored broya ribari
# proverka dali e esen, za da vidim cenata smenya li se
# budget - pari = needed_money
# proverka dali budgeta >= price-a, ako ne e stigat da e s minus needed_money
price = 0

if season == "Spring":
    price = 3000
elif season == "Summer" or season == "Autumn":
    price = 4200
elif season == "Winter":
    price = 2600

if count_of_people <= 6:
    price = price - price * 0.10
elif 7 <= count_of_people <= 11:
    price = price - price * 0.15
elif count_of_people >= 12:
    price = price - price * 0.25


if season == "Autumn" and count_of_people % 2 == 0:
    price = price
elif count_of_people % 2 == 0:
    price = price - price * 0.05

needed_money = budget - price

if budget >= price:
    print(f"Yes! You have {needed_money:.2f} leva left.")
elif budget < price:
    print(f"Not enough money! You need {-needed_money:.2f} leva.")
