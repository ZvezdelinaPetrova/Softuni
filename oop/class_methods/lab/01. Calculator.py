from collections import deque


class Calculator:
    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def multiply(*args):
        result = 1
        for x in args:
            result *= x
        return result

    @staticmethod
    def divide(*args):
        args = deque(args)
        f = args.popleft()
        result = f
        for x in args:
            if x != 0:
                result /= x
        return result

    @staticmethod
    def subtract(*args):
        args = deque(args)
        f = args.popleft()
        result = f
        for x in args:
            result -= x
        return result


# from functools import reduce
#
#
# class Calculator:
#
#     @staticmethod
#     def add(*args):
#         result = reduce(lambda a, b: a + b, args)
#         return result
#
#     @staticmethod
#     def multiply(*args):
#         result = reduce(lambda a, b: a * b, args)
#         return result
#
#     @staticmethod
#     def divide(*args):
#         result = reduce(lambda a, b: a / b, args)
#         return result
#
#     @staticmethod
#     def subtract(*args):
#         result = reduce(lambda a, b: a - b, args)
#         return result
#
#
# print(Calculator.add(5, 10, 4))
# print(Calculator.multiply(1, 2, 3, 5))
# print(Calculator.divide(100, 2))
# print(Calculator.subtract(90, 20, -50, 43, 7))
