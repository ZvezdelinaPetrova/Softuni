def naughty_or_nice_list(*args, **kwargs):
    result = ""
    nice = []
    naughty = []
    not_found = []
    tuples_list = args[0]
    new_dict = {}
    for el in tuples_list:
        number, name = el[0], el[1]
        if number not in new_dict:
            new_dict[number] = []
            new_dict[number].append(name)
        else:
            new_dict[number].append(name)

    strings_list = args[1:]
    for x in strings_list:
        which_number, word = x.split("-")
        which_number = int(which_number)
        if word == "Naughty":
            if (which_number in new_dict) and len(new_dict[which_number]) == 1:
                naughty.append(new_dict[which_number][0])
                new_dict.pop(which_number)
        elif word == "Nice":
            if (which_number in new_dict) and len(new_dict[which_number]) == 1:
                nice.append(new_dict[which_number][0])
                new_dict.pop(which_number)

    for key, value in new_dict.items():
        for b in value:
            not_found.append(b)

    if kwargs:
        for k, v in kwargs.items():
            x = not_found.count(k)
            if x == 1:
                if v == "Naughty":
                    naughty.append(k)
                    not_found.remove(k)
                elif v == "Nice":
                    nice.append(k)
                    not_found.remove(k)

    if nice:
        result += f"Nice: {', '.join(str(x) for x in nice)}" + "\n"
    if naughty:
        result += f"Naughty: {', '.join(str(x) for x in naughty)}" + "\n"
    if not_found:
        result += f"Not found: {', '.join(str(x) for x in not_found)}"

    return result


# print(naughty_or_nice_list([(3, "Amy"), (1, "Tom"), (7, "George"), (3, "Katy"), ], "3-Nice", "1-Naughty",
#                            Amy="Nice", Katy="Naughty",))
# print(naughty_or_nice_list(
#     [
#         (7, "Peter"),
#         (1, "Lilly"),
#         (2, "Peter"),
#         (12, "Peter"),
#         (3, "Simon"),
#     ],
#     "3-Nice",
#     "5-Naughty",
#     "2-Nice",
#     "1-Nice",
#     ))

print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))
