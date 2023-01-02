number = int(input())

total = 0
current_symbol = 0

for i in range(1, number + 1):
    new_number = str(i)
    total = 0
    for j in new_number:
        current_symbol = int(j)
        total += current_symbol
    if total == 5 or total == 7 or total == 11:
        print(f"{i} -> True")
    else:
        print(f"{i} -> False")




