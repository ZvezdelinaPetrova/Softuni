searched_word = input()
data = input()

final_string = ""
while searched_word in data:
    data = data.replace(searched_word, "")
print(data)