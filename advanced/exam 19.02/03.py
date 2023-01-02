def start_spring(**kwargs):
    new_dict = kwargs
    searched_dict = {}
    more_than_two = False
    for key, value in new_dict.items():
        if value not in searched_dict:
            searched_dict[value] = []
            searched_dict[value].append(key)
        else:
            searched_dict[value].append(key)
    numbers = []
    for key, value in searched_dict.items():
        current_el_len = len(searched_dict[key])
        numbers.append(current_el_len)
    len_1 = len(numbers)
    len_2 = set(numbers)
    if len_1 != len(len_2):
        more_than_two = True

    ordered_by_name = sorted(new_dict, key = lambda k: (-len(new_dict[k]), k))

    scenario_1 = {}
    for element in ordered_by_name.split():
        scenario_1[element] = searched_dict[element]

    end_string = ''

    # обхождам въпросния стринг и печатя елементите му, след което за същия ключ печатя и стойностите.
    for element in ordered_by_name.split():
        end_string = end_string + element + ":" + '\n'
        for val in scenario_1[element]:
            end_string = end_string + "-" + val + '\n'
    return end_string


example_objects = {"Water Lilly": "flower",
                       "Swifts": "bird",
                       "Callery Pear": "tree",
                       "Swallows": "bird",
                       "Dahlia": "flower",
                       "Tulip": "flower"}
print(start_spring(**example_objects))
#
# example_objects = {"Swallow": "bird",
#                    "Thrushes": "bird",
#                    "Woodpeckers": "bird",
#                    "Swallows": "bird",
#                    "Warblers": "bird",
#                    "Shrikes": "bird"}
# print(start_spring(**example_objects))
#
# example_objects = {"Magnolia": "tree",
#                    "Swallow": "bird",
#                    "Thrushes": "bird",
#                    "Pear": "tree",
#                    "Cherries": "tree",
#                    "Shrikes": "bird",
#                    "Butterfly": "insect"}
# print(start_spring(**example_objects))


# "{" + "\n".join("{!r}: {!r},".format(k, v) for k, v in test_1.items()) + "}"

# # обхождам въпросния стринг и печатя елементите му, след което за същия ключ печатя и стойностите.
# for element in key_order.split():
#     print(element + ":")
#     for val in searched_dict[element]:
#         print("-" + val)

# ordered_by_name = ' '.join(sorted(searched_dict, key=lambda k: len(searched_dict[k]), reverse=True))