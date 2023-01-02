n = int(input())
current_number = 1
counter = 0
n_is_bigger_than_current = False
for row in range(1, n + 1):
    for column in range(1, row + 1):
        if current_number > n:
            n_is_bigger_than_current = True
            break
        print(str(current_number) + " ", end="")
        current_number += 1
    if n_is_bigger_than_current:
        break
    print()
