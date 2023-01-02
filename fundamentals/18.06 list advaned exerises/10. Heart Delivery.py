neighbourhood = [int(el) for el in input().split("@")]

failed = 0
command = input()
last_position = 0
successful = True

while command != "Love!":
    command, length = command.split()
    last_position += int(length)
    if 0 <= last_position <= len(neighbourhood) - 1:
        if neighbourhood[last_position] == 0:
            print(f"Place {last_position} already had Valentine's day.")
        elif neighbourhood[last_position] > 0:
            neighbourhood[last_position] -= 2
            if neighbourhood[last_position] == 0:
                print(f"Place {last_position} has Valentine's day.")
    else:
        last_position = 0
        if neighbourhood[last_position] == 0:
            print(f"Place {last_position} already had Valentine's day.")
        elif neighbourhood[last_position] > 0:
            neighbourhood[last_position] -= 2
            if neighbourhood[last_position] == 0:
                print(f"Place {last_position} has Valentine's day.")
    command = input()


for el in neighbourhood:
    if el != 0:
        failed += 1
        successful = False

print(f"Cupid's last position was {last_position}.")

if successful:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {failed} places.")