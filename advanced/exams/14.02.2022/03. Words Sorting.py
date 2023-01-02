def words_sorting(*args):
    new_dict = {}
    for el in args:
        result = 0
        for ch in el:
            result += ord(ch)
        new_dict[el] = result

    sum_all = 0
    for key, value in new_dict.items():
        sum_all += value

    if sum_all % 2 == 0:
        final = ""
        for k, v in sorted(new_dict.items()):
            final += f"{k} - {v}" + "\n"
        return final.strip()
    elif sum_all % 2 == 1:
        test = sorted(new_dict.items(), key=lambda x: -x[1])
        final = ""
        for k, v in test:
            final += f"{k} - {v}" + "\n"
        return final.strip()

# print(
#     words_sorting(
#         'escape',
#         'charm',
#         'mythology'
#   ))

# print(
#     words_sorting(
#         'escape',
#         'charm',
#         'eye'
#   ))

print(
    words_sorting(
        'cacophony',
        'accolade'
  ))

