data = input()

list_with_last_opening_bracket = []


for i in range(len(data)):
    if data[i] == "(":
        list_with_last_opening_bracket.append(i)
    elif data[i] == ")":
        start_text = list_with_last_opening_bracket.pop()
        end_index = i
        combo = data[start_text: end_index + 1]
        print(f"{combo}")

# text = input()
# new_text = [x for x in text]
#
# searched_p = []
#
# for index in range(len(new_text)):
#     if new_text[index] == "(":
#         searched_p.append(index)
#     elif new_text[index] == ")":
#         searched_p.append(index)
#         end = searched_p.pop()
#         beginning = searched_p.pop()
#         print(text[beginning:end + 1])