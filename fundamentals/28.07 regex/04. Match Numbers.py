import re

pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"
data = input()
my = [i.group() for i in re.finditer(pattern, data)]
print(*my, sep=" ")