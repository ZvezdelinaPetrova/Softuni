data = [int(x) for x in input().split()]
expected_result = int(input())
count = 0

pairs = set()

for x in range(len(data)):
    current_number = data[x]
    current_list = data[(x + 1):]
    for j in current_list:
        count += 1
        if current_number + j == expected_result:
            print(f"{current_number} + {j} = {expected_result}")
            pair_to_add = current_number, j
            pairs.add(pair_to_add)

print(f"Iterations done: {count}")

for x in pairs:
    print(x)

# Ако не направя на сет двойките, демек да направя лист с уникални двойки и след това да ги принтирам
# unique = []

# for x in pairs:
#     if x in unique:
#         continue
#     else:
#         unique.append(x)
#         number_1 = x[0]
#         number_2 = x[1]
#         print(f"({number_1}, {number_2})")