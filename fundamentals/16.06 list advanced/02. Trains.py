train_wagons = int(input())
wagons_all = [0] * train_wagons

command = input()

while command != "End":
    action = command.split()
    if action[0] == "add":
        wagons_all[-1] += int(action[1])
    elif action[0] == "insert":
        index = int(action[1])
        wagons_all[index] += int(action[2])
    elif action[0] == "leave":
        index = int(action[1])
        wagons_all[index] -= int(action[2])
    command = input()

print(wagons_all)