import re

pattern = r"\d+"

text = input()
while text:
    matches = re.finditer(pattern, text)
    for match in matches:
        print(match.group(), end=" ")
    text = input()