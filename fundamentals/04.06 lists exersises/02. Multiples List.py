number = int(input())
count = int(input())

new_list = []
counter = 0

while len(new_list) < count:
    counter += 1
    if counter % number == 0:
        new_list.append(counter)

print(new_list)