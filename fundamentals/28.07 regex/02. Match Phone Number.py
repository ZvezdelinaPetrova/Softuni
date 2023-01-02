import re

pattern = r"\+359+(?P<delimiter>[-\s])2(?P=delimiter)2{3}(?P=delimiter)2{4}\b"
data = input()
my = [i.group() for i in re.finditer(pattern, data)]
print(*my, sep=", ")


