new_list = input().split()
number = int(input())

list_numbers = []
final_list = []
for i in range(number):
    list_numbers = []
    for j in new_list:
        new_number = int(j)
        list_numbers.append(new_number)
    min_number = min(list_numbers)
    list_numbers.remove(min_number)
    new_list = list_numbers

for m in range(len(new_list)):
    new_str = str(new_list[m])
    final_list.append(new_str)

separator = ", "
print(separator.join(final_list))
