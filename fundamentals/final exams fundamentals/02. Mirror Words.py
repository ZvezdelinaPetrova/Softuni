import re

pattern = r"(#|@)(?P<first_word>[a-zA-Z]{3,})\1{2}(?P<second_word>[a-zA-Z]{3,})\1"

data = input()

matches = [i.group() for i in re.finditer(pattern, data)]
if len(matches) == 0:
    print("No word pairs found!")
else:
    print(f"{len(matches)} word pairs found!")
all_matches = []
for i in re.finditer(pattern, data):
    f = i.group()
    b = i.groupdict()
    first = b["first_word"]
    second = b["second_word"]
    reversed_second = second[::-1]
    if first == reversed_second:
        all_matches.append(first)

new_list = []

if len(all_matches) == 0:
    print("No mirror words!")
else:
    print("The mirror words are:")
    for i in all_matches:
        r = i[::-1]
        text = (i + " <=> " + r)
        new_list.append(text)
    print(*new_list, sep=", ")
