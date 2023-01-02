targets = [int(el) for el in input().split()]

count = 0
command = input()

while command != "End":
    index = int(command)
    if 0 <= index < len(targets):
        current_number = targets[index]
        count += 1
        targets[index] = -1
        for b in range(len(targets)):
            if current_number < targets[b]:
                if targets[b] == -1:
                    continue
                targets[b] -= current_number
            elif current_number >= targets[b]:
                if targets[b] == -1:
                    continue
                targets[b] += current_number

    command = input()

str_list = [str(el) for el in targets]


print(f"Shot targets: {count} -> {' '.join(str_list)}")