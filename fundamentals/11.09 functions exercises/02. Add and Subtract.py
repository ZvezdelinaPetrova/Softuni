def sum_numbers(num_1, num_2):
    return num_1 + num_2


# def subtract(result, num_3):
#     result = sum_numbers(number_1, number_2)
#     return result - num_3


def add_and_subtract(num_1, num_2, num_3):
    condition_1 = sum_numbers(num_1, num_2)
    return condition_1 - num_3


number_1 = int(input())
number_2 = int(input())
number_3 = int(input())

print(add_and_subtract(number_1, number_2, number_3))