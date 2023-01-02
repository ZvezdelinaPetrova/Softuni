numbers = [int(el) for el in input().split()]
sum_of_all = sum(numbers)
average = sum_of_all / len(numbers)

new_list = []
descending_list = []
no_bigger = False
counter = 0

for j in numbers:
    if j > average:
        new_list.append(j)
        counter += 1

if counter == 0:
    no_bigger = True

if len(new_list) > 5:
    while len(new_list) > 5:
        minimum = min(new_list)
        item_to_delete = new_list.index(minimum)
        new_list.pop(item_to_delete)

new_list = sorted(new_list)

for i in range(len(new_list)-1, -1, -1):
    descending_list.append(new_list[i])

if not no_bigger:
    print(*descending_list)
else:
    print("No")