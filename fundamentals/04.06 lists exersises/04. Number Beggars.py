numbers = input().split(", ")
beggars = int(input())

final_list = []
counter = 0
for j in range(1, beggars + 1):
    counter = 0
    for i in range(0, len(numbers), beggars):
        counter += int(numbers[i])
    final_list.append(counter)
    if len(numbers) > 0:
        numbers.pop(0)
print(final_list)


