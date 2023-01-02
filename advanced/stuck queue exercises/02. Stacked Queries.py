n = int(input())

new_list = []
reversed_list = []

for _ in range(n):
    data = input().split()
    first = data[0]
    if first == "1":
        number_to_push = data[1]
        new_list.append(number_to_push)
    elif first == "2":
        if len(new_list) >= 1:
            new_list.pop()
    elif first == "3":
        if len(new_list) >= 1:
            print(max(new_list))
    elif first == "4":
        if len(new_list) >= 1:
            print(min(new_list))

while new_list:
    reversed_letter = new_list.pop()
    reversed_list.append(reversed_letter)
print(", ".join(reversed_list))

# print(f"{', '.join(str(x) for x in reversed(new_list))}")