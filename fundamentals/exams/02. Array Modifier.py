integers = [int(el) for el in input().split()]

command = input()

while command != "end":
    command = command.split()
    if command[0] == "swap":
        index_as_int = int(command[1])
        index_2_as_int = int(command[2])
        integers[index_as_int], integers[index_2_as_int] = integers[index_2_as_int], integers[index_as_int]
    elif command[0] == "multiply":
        index_as_int = int(command[1])
        index_2_as_int = int(command[2])
        result = integers[index_as_int] * integers[index_2_as_int]
        integers.pop(index_as_int)
        integers.insert(index_as_int, result)
    elif command[0] == "decrease":
        for el in range(len(integers)):
            integers[el] -= 1
    command = input()

print(*integers, sep=', ')