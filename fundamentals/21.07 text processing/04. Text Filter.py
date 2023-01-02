words_to_delete = input().split(", ")
text = input()

for word in words_to_delete:
    if word in text:
        text = text.replace(word, "*"*len(word))
print(text)