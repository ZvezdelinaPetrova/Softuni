import re
text = input()

pattern = r'\b\_(?P<variable_name>[A-Za-z0-9]+)\b'
new_list = []

my = re.finditer(pattern, text)
for i in my:
    new_list.append(i.group('variable_name'))

print(','.join(new_list))

