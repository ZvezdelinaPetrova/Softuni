import re

data = input()

pattern = r"([@|#]{1,})(?P<color>[a-z]{3,})([_\W.*)([\/]{1,})(?P<amount>\d+)([\/]{1,})"

for i in re.finditer(pattern, data):
    b = i.groupdict()
    color = b["color"]
    amount = b["amount"]
    print(f"You found {amount} {color} eggs!")