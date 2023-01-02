text = input().split()

final_list = []

for el in text:
    numbers = []
    string_list = []
    z = []
    for letter in el:
        if letter.isnumeric():
            numbers.append(letter)
        else:
            string_list.append(letter)
    n = chr(int("".join(numbers)))
    z.append(n)
    final_list = z + string_list
    final_list[1], final_list[-1] = final_list[-1], final_list[1]
    print("".join(final_list), end=" ")