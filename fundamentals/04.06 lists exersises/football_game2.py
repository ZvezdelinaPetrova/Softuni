cards = input().split()
team_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
team_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
game_end = False
counter_a = 11
counter_b = 11

for i in range(len(cards)):
    cards_n = cards[i]
    new = cards_n.split("-")

