cards = input().split()
team_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
team_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
game_end = False
counter_a = 11
counter_b = 11

for i in cards:
    card = i.split("-")
    current_team = card[0]
    current_player = int(card[1])
    if current_team == "A" and current_player in team_a:
        team_a.remove(current_player)
        counter_a -= 1
        if counter_a < 7:
            game_end = True
            break
    elif current_team == "B" and current_player in team_b:
        team_b.remove(current_player)
        counter_b -= 1
        if counter_a < 7:
            game_end = True
            break

print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")

if game_end:
    print("Game was terminated")