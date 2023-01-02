def func_executor(*args):
    result = ""
    for k, v in args:
        fun_result = k(*v)
        result += f"{k.__name__} - {fun_result}" + "\n"
    return result.strip()

# викане на функция и резутата и

# def func_executor(*args):
#     result = []
#     for name, numbers in args:
#         result.append(name(*numbers))
#     return result
#
#
# def sum_numbers(num1, num2):
#     return num1 + num2
#
#
# def multiply_numbers(num1, num2):
#     return num1 * num2


# print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))