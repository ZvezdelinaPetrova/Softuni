data = input().split("\\")

searched_word = data[-1]

split_searched_word = searched_word.split(".")

print(f"File name: {split_searched_word[0]}")
print(f"File extension: {split_searched_word[1]}")








