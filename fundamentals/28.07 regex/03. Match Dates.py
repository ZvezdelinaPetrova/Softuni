import re

pattern = r"\b\d{2}(?P<sep>[-/\.])[A-Z][a-z]{2}(?P=sep)\d{4}\b"
data = input()
my = [i.group() for i in re.finditer(pattern, data)]
for i in my:
    day = i[0:2]
    month = i[3:6]
    year = i[7:11]
    print(f"Day: {day}, Month: {month}, Year: {year}")
