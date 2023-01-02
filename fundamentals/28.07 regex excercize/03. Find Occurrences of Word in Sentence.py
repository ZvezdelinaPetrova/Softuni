import re

text = input()
searched_word = input()
pattern = rf"\b{searched_word}\b"

my = re.findall(pattern, text, flags=re.IGNORECASE)
print(len(my))

