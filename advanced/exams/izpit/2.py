from collections import deque


def valid_index(one, two):
    if 0 <= one < row and 0 <= two < row:
        return True


players = deque(input().split(", "))

row = 6

matrix = []

for r in range(row):
    matrix.append(input().split())

winner = ""
rest_list = []
while True:
    command = input()
    o = command[1:-1]
    f, s = o.split(", ")
    index_1 = int(f)
    index_2 = int(s)
    current_player = players.popleft()
    if rest_list:
        if rest_list[0] == current_player:
            rest_list.remove(current_player)
            players.append(current_player)
            continue
    if valid_index(index_1, index_2):
        if matrix[index_1][index_2] == "E":
            winner = current_player
            print(f"{current_player} found the Exit and wins the game!")
            break
        elif matrix[index_1][index_2] == "T":
            if current_player == "Jerry":
                winner = "Tom"
            else:
                winner = "Jerry"
            print(f"{current_player} is out of the game! The winner is {winner}.")
            break
        elif matrix[index_1][index_2] == "W":
            print(f"{current_player} hits a wall and needs to rest.")
            rest_list.append(current_player)

    players.append(current_player)