import sys

command = input()

greater_number = - sys.maxsize

while command != "Stop":
    number = int(command)
    if greater_number < number:
        greater_number = number
    command = input()
print(greater_number)
