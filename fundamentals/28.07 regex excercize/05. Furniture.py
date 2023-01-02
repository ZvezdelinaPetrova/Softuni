import re

pattern = r">{2}(?P<name>[A-Za-z]+)<{2}(?P<price>\d+(\.\d+)?)\!(?P<quantity>\d+)"

command = input()
total = 0
all_items = []
while not command == "Purchase":
    valid_command = re.finditer(pattern, command)
    for i in valid_command:
        total += float(i["price"]) * int(i["quantity"])
        all_items.append(i["name"])
    command = input()

print("Bought furniture:")
for j in all_items:
    print(j)
print(f"Total money spend: {total:.2f}")