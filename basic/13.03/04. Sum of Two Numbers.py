x1 = int(input())
x2 = int(input())
magic = int(input())

counter = 0
is_magic_number = False

#Ако е намерена комбинация чиито сбор на числата е равен на магическото число
#Combination N:{пореден номер} ({първото число} + {второ число} = {магическото число})"
#Ако не е намерена комбинация отговаряща на условието
#"{броят на всички комбинации} combinations - neither equals {магическото число}"""

for first in range(x1, x2 + 1):
    for second in range(x1, x2 + 1):
        result = first + second
        counter += 1
        if result == magic:
            is_magic_number = True
            print(f"Combination N:{counter} ({first} + {second} = {result})")
            break
    if is_magic_number:
        break
if not is_magic_number:
    print(f"{counter} combinations - neither equals {magic}")

# if not true e tova- koeto e taka, zashoto tya ne e true, ami e false tazi promenliva!!!!


