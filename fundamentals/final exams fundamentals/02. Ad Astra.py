import re

pattern = r"(#|\|)(?P<product>[A-Za-z\s]{1,})\1(?P<date>\d{2}/\d{2}/\d{2})\1(?P<calories>\d+)\1"

data = input()
calories = 0
new_list = []
for i in re.finditer(pattern, data):
    b = i.groupdict()
    first = b["calories"]
    calories += int(first)
days = calories // 2000

print(f"You have food to last you for: {days} days!")
for j in re.finditer(pattern, data):
    b = j.groupdict()
    item_name = b["product"]
    expiration_date = b["date"]
    calories_final = b["calories"]
    print(f"Item: {item_name}, Best before: {expiration_date}, Nutrition: {calories_final}")
