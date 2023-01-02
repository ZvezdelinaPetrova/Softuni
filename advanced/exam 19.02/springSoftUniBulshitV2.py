from cgi import test


def start_spring(**kwargs):

    new_dict = {}

    # Обхождам входящия речник.Валюто от входящия речник трябва да стане ключ в новия речник.
    for key, value in kwargs.items():
        # ако валюто я няма като ключ в новия я добавам, първо с празен list, след това добавям към листа и ключа
        if value not in new_dict:
            new_dict[value] = []
            new_dict[value].append(key)
        # ако я има просто добавям стария ключ като валю към новия речник
        else:
            new_dict[value].append(key)



    # Обхождам новия речник и сортирам първо ресултатите в lista (values)
    for key,value in new_dict.items():
        new_dict[key] = sorted(value)

    # Връща лист с подредените ключове по дължина на value и по азбучен ред
    key_order = sorted(new_dict, key = lambda k: (-len(new_dict[k]), k))

    end_strg = ''

    # обхождам въпросния лист и добавям елементите му към стринга, след което за същия ключ добавям и value-тата.
    for element in key_order:
        end_strg = end_strg + element + ":" + '\n'
        for val in new_dict[element]:
            end_strg = end_strg + "-" + val + '\n'

    return end_strg



example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird",}
print(start_spring(**example_objects))



