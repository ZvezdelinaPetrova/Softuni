import re

pattern = r"(\=|\/)(?P<destination>[A-Z][A-Za-z]{2,})\1"

data = input()
travel_points = 0

all_matches = []
for i in re.finditer(pattern, data):
    b = i.groupdict()
    first = b["destination"]
    travel_points += len(first)
    all_matches.append(first)


print(f"Destinations: {', '.join(all_matches)}")
print(f"Travel Points: {travel_points}")