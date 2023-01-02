data = input().split()
new_word = ""
for word in data:
    new_word += word * len(word)
print(f"{new_word}")

    