from collections import deque


def valid_index(one, two):
    if 0 <= one < row and 0 <= two < row:
        return True


players = deque(input().split(","))
players_dict = {}
for x in players:
    players_dict[x] = 501

trows_dict = {}
for x in players_dict:
    trows_dict[x] = 0

row = 7

matrix = []

for r in range(row):
    matrix.append(input().split())

winner = ""

while True:
    command = input()
    o = command[1:-1]
    f, s = o.split(", ")
    index_1 = int(f)
    index_2 = int(s)
    current_player = players.popleft()
    trows_dict[current_player] += 1
    if valid_index(index_1, index_2):
        if matrix[index_1][index_2] == "B":
            winner = current_player
            break
        elif matrix[index_1][index_2].isdigit():
            players_dict[current_player] -= int(matrix[index_1][index_2])

        elif matrix[index_1][index_2] == "T":
            result = (int(matrix[0][index_2]) + int(matrix[index_1][6])
                      + int(matrix[index_1][0]) + int(matrix[6][index_2])) * 3
            players_dict[current_player] -= result

        elif matrix[index_1][index_2] == "D":
            result = (int(matrix[0][index_2]) + int(matrix[index_1][6]) +
                      int(matrix[index_1][0]) + int(matrix[6][index_2])) * 2
            players_dict[current_player] -= result

    if players_dict[current_player] <= 0:
        winner = current_player
        break
    players.append(current_player)

print(f"{current_player} won the game with {trows_dict[current_player]} throws!")