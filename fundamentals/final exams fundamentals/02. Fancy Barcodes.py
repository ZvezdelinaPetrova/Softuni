import re
n = int(input())

pattern = r"(@#+)([A-Z][A-Za-z0-9]{4,}[A-Z])(@#+)"

number = ''

for i in range(n):
    data = input()
    match = re.search(pattern, data)
    if match:
        list_with_matches = [i.group() for i in re.finditer(pattern, data)]
        number = ''
        for match in list_with_matches:
            for char in match:
                if char.isdigit():
                    number += char
            if number == '':
                print(f"Product group: 00")
            else:
                print(f"Product group: {int(number)}")
    else:
        print("Invalid barcode")

# import re
# pattern = r'(@#+)([A-Z][A-Za-z0-9]{4,}[A-Z])(@#+)'
# digits = r'\d'
# n = int(input())
# for _ in range(n):
#     s = input()
#     m = re.fullmatch(pattern, s)
#     if m:
#         product_group = '00'
#         current_digits = re.findall(digits, s)
#         if current_digits:
#             product_group = ''.join(current_digits)
#         print(f'Product group: {product_group}')
#     else:
#         print(f"Invalid barcode")