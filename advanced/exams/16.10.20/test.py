from functools import reduce


def get_magic_triangle(number):

    matrix = []
    for x in range(1, number + 1):
        matrix.append([1] * x)

    for g in range(number):
        current_list = matrix[g]
        if matrix[g + 1]:
            next_list = matrix[g + 1]



    return matrix


print(get_magic_triangle(5))