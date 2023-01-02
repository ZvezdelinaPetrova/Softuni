import re

data = input()

pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"

m = re.findall(pattern, data)

print(" ".join(m))

