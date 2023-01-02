words = input().split()

new_list = [el for el in words if len(el) % 2 == 0]

for i in new_list:
    print(i)