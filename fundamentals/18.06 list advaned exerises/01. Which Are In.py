first_string = input().split(", ")
second_string = input().split(", ")

new_list = []

for i in first_string:
    for j in second_string:
        if i in j:
            new_list.append(i)
print(sorted(set(new_list), key=first_string.index))