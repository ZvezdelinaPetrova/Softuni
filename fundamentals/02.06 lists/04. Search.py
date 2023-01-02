number = int(input())
word = input()

words_list = []
list_2 = []
for i in range(number):
    new_text = input()
    words_list.append(new_text)
    if word in new_text:
        list_2.append(new_text)
print(words_list)
print(list_2)

