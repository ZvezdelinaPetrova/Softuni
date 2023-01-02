data = [int(i) for i in input().split()]
new_list = []

while data:
    new_list.append(data.pop())
print(*new_list, end=" ")

data = input().split()

# new_list = []
#
# for x in range(len(data)):
#     current_number = data.pop()
#     new_list.append(current_number)
#
# print(f'{" ".join(x for x in new_list)}')


# data = input()
#
# new_list = data[::-1]
#
# print(new_list)