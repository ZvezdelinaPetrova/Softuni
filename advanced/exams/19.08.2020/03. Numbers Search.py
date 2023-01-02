def numbers_searching(*args):
    unique = []
    duplicates = []
    missing = ""
    for x in args:
        if x not in unique:
            unique.append(x)
        else:
            duplicates.append(x)
    smallest = min(unique)
    biggest = max(unique)
    new_list = []
    new_list.extend(range(smallest, biggest + 1))
    for el in new_list:
        if el not in unique:
            missing = el
    duplicates = set(duplicates)
    final_list = []
    final_list.append(missing)
    final_list.append([x for x in sorted(duplicates)])
    return final_list

# import collections


# def numbers_searching(*args):
#     numbers = list(args)
#     duplicates = set([x for x in numbers if numbers.count(x) > 1])
#     duplicates_list = list(duplicates)
#     # start = numbers[0]
#     # end = numbers[-1]
#     start = min(numbers)
#     end = max(numbers)
#     missing_number = sorted(set(range(start, end + 1)).difference(numbers))
#     return list((*missing_number, sorted(duplicates_list)))


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))