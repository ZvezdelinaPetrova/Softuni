def result(what_to_do, number_1, number_2):
    if what_to_do == "multiply":
        return number_1 * number_2
    elif what_to_do == "divide":
        return int(number_1 / number_2)
    elif what_to_do == "subtract":
        return number_1 - number_2
    elif what_to_do == "add":
        return number_1 + number_2


action = input()
num_1 = int(input())
num_2 = int(input())

print(result(action, num_1, num_2))
