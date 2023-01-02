import re

pattern = r"(?P<separator>\:{2}|\*{2})(?P<word>[A-Z][a-z]{2,})(?P=separator)"

counter = 0
# cool_emo_list = []
to_be_cool = 1
data = input()
new_list = []
# len_of_emo = len(re.findall(pattern, data))
# emojis = [i.group() for i in re.finditer(pattern, data)] - taka se pravi na list
emojis = re.finditer(pattern, data)
for i in emojis:
    new_list.append(i.group())

len_of_emo = len(new_list)

for char in data:
    if char.isdigit():
        to_be_cool = to_be_cool * int(char)


print(f"Cool threshold: {to_be_cool}")
print(f"{len_of_emo} emojis found in the text. The cool ones are:")
for emoji in new_list:
    counter = 0
    matches = re.search(pattern, emoji)
    test = matches.group("word")
    for h in test:
        counter += ord(h)
    if counter >= to_be_cool:
        print(f"{emoji}")
