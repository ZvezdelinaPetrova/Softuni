first = set(int(x) for x in input().split())
second = set(int(x) for x in input().split())

number = int(input())

for x in range(number):
    current_row = input().split()
    command = current_row[0]
    which_set = current_row[1]
    numbers = current_row[2:]
    if command == "Add" and which_set == "First":
        for j in numbers:
            first.add(int(j))
    elif command == "Add" and which_set == "Second":
        for m in numbers:
            second.add(int(m))
    elif command == "Remove" and which_set == "First":
        for j in numbers:
            if int(j) in first:
                first.remove(int(j))
    elif command == "Remove" and which_set == "Second":
        second = second.difference(numbers)
        for m in numbers:
            if int(m) in second:
                second.remove(int(m))
    else:
        if first.issubset(second) or second.issubset(first):
            print("True")
        else:
            print("False")

if first:
    print(f"{', '.join(str(x) for x in sorted(first))}")
if second:
    print(f"{', '.join(str(x) for x in sorted(second))}")

#
# first = set(int(x) for x in input().split())
# second = set(int(x) for x in input().split())
#
# n = int(input())
#
# for _ in range(n):
#     command = input().split()
#     action = command[0]
#     which_set = command[1]
#     numbers = command[2:]
#     if action == "Add" and which_set == "First":
#         [first.add(int(x)) for x in numbers]
#     elif action == "Add" and which_set == "Second":
#         [second.add(int(x)) for x in numbers]
#     elif action == "Remove" and which_set == "First":
#         current_set = [(int(x)) for x in numbers]
#         first = first.difference(current_set)
#     elif action == "Remove" and which_set == "Second":
#         current_set = [(int(x)) for x in numbers]
#         second = second.difference(current_set)
#     else:
#         if first.issubset(second) or second.issubset(first):
#             print("True")
#         else:
#             print("False")
#
# print(", ".join(str(i) for i in sorted(first)))
# print(", ".join(str(i) for i in sorted(second)))
