def even_odd_filter(**kwargs):
    new_dict = {}
    for command in kwargs:
        needed_list = kwargs[command]
        if command == "odd":
            new_dict[command] = [x for x in needed_list if x % 2 == 1]
        elif command == "even":
            new_dict[command] = [x for x in needed_list if x % 2 == 0]

    test = sorted(new_dict.items(), key=lambda x: -len(x[1]))
    f = {}
    for k, v in test:
        f[k] = v
    return f


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))

print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))
