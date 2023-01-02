def numbers(ns):
    negative = []
    positive = []
    for x in ns:
        if x < 0:
            negative.append(x)
        else:
            positive.append(x)
    result = ""
    result += f"{sum(negative)}" + "\n"
    result += f"{sum(positive)}" + "\n"
    if abs(sum(negative)) > sum(positive):
        result += f"The negatives are stronger than the positives"
    else:
        result += f"The positives are stronger than the negatives"
    return result


data = [int(x) for x in input().split()]

print(numbers(data))

# /////////////////////////////////////////////////////////////////
# numbers = [int(x) for x in input().split()]
#
# negative = []
# positive = []
#
# for el in numbers:
#     if el > 0:
#         positive.append(el)
#     else:
#         negative.append(el)
#
# sum_negative = sum(negative)
# sum_positive = sum(positive)
#
# print(sum_negative)
# print(sum_positive)
#
#
# if abs(sum_negative) > abs(sum_positive):
#     print(f"The negatives are stronger than the positives")
# else:
#     print(f"The positives are stronger than the negatives")

# //////////////////////////////////////////////////

# nums = [int(el) for el in input().split()]
#
# negative_sum = sum(filter(lambda x: x < 0, nums))
# print(negative_sum)
# positive_sum = sum(filter(lambda x: x >= 0, nums))
# print(positive_sum)
#
# if abs(negative_sum) > positive_sum:
#     print("The negatives are stronger than the positives")
# else:
#     print("The positives are stronger than the negatives")

