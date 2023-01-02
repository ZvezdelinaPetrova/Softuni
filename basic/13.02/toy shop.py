#pechalba pri porachka ot poveche ot 50 igrachki procent ostapka 25% ot obshtata cena
#10% se vzimat ot pechalbata za naem, za da stane pechalba
#пари за екскурзия - пари от печалба

vacation_price = float(input())
how_many_puzzles = int(input())
how_many_dolls = int(input())
how_many_bears = int(input())
how_many_minions = int(input())
how_many_trucks = int(input())
puzzle_price = how_many_puzzles * 2.6
dolls_price = how_many_dolls * 3
bears_price = how_many_bears * 4.10
minion_price = how_many_minions * 8.20
trucks_price = how_many_trucks * 2

all_toys = how_many_puzzles + how_many_dolls + how_many_bears + how_many_minions + how_many_trucks
profit_from_all = puzzle_price + dolls_price + bears_price + minion_price + trucks_price

if all_toys >= 50:
    discount = profit_from_all * 0.25
    profit = profit_from_all - discount
else:
    profit = profit_from_all

rent = profit * 0.1

money_for_vacation = profit - rent

if money_for_vacation >= vacation_price:
    left_money = money_for_vacation - vacation_price
    print(f"Yes! {left_money:.2f} lv left.")

if money_for_vacation < vacation_price:
    left_money = vacation_price - money_for_vacation
    print(f"Not enough money! {left_money:.2f} lv needed.")
