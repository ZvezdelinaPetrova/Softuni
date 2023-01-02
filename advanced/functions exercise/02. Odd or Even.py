def even_odd(*args):
    command = args[-1]
    needed_list = args[:-1]
    result = ""
    if command == "odd":
        result = [x for x in needed_list if x % 2 == 1]
    elif command == "even":
        result = [x for x in needed_list if x % 2 == 0]
    return result


# command = input()
#
# numbers = [int(x) for x in input().split()]
#
# count = len(numbers)
#
# result = 0
#
# if command == "Even":
#     result = sum([int(x) for x in numbers if x % 2 == 0])
#     result = result * count
# else:
#     result = sum([int(x) for x in numbers if x % 2 == 1])
#     result = result * count
#
# print(result)



# from functools import reduce
#
#
# def odd_or_even_sum(command, nums):
#     if command == "Odd":
#         odd_nums = list(filter(lambda x: x % 2 == 1, nums))
#         sum_nums = reduce(lambda a, b: a+b, odd_nums)
#     else:
#         even_nums = list(filter(lambda x: x % 2 == 0, nums))
#         sum_nums = reduce(lambda a, b: a + b, even_nums)
#     return sum_nums * len(nums)
#
#
# command_line = input()
# numbers = [int(el) for el in input().split()]
# print(odd_or_even_sum(command_line, numbers))