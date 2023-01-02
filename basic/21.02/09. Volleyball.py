from math import floor

year_type = input()
count_of_vacation = int(input())
count_outside_of_sofia = int(input())


weekends = 48
weekends_in_sofia = weekends - count_outside_of_sofia
games_in_sofia = (weekends_in_sofia * 3) / 4
games_in_vacation = count_of_vacation * 2 / 3
total_games = games_in_sofia + games_in_vacation + count_outside_of_sofia

if year_type == "leap":
    total_games += total_games * 0.15
elif year_type == "normal":
    total_games = total_games

print(floor(total_games))




