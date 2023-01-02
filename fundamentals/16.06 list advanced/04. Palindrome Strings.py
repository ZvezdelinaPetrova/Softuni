words = input().split()
searched_word = input()
counter = 0

new_list = [word for word in words if word == word[::-1]]

# for word in words:
#     if word == word[::-1]:
#         new_list.append(word)
print(new_list)

for word in words:
    if searched_word == word:
        counter += 1
print(f"Found palindrome {counter} times")

#new_list.count(searched_word)- пак дава две