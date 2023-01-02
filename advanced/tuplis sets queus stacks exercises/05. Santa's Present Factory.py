from collections import deque

materials = deque(int(x) for x in input().split())  # last
magic = deque(int(x) for x in input().split())  # first

presents = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}

toys_crafted = {}

while materials and magic:
    current_material = materials.pop()
    current_magic = magic.popleft()
    if current_material == 0 and current_magic == 0:
        continue
    if current_magic == 0:
        materials.append(current_material)
        continue
    if current_material == 0:
        magic.appendleft(current_magic)
        continue

    result = current_material * current_magic

    if result in presents:
        toy_name = presents[result]
        if toy_name not in toys_crafted:
            toys_crafted[toy_name] = 1
        else:
            toys_crafted[toy_name] += 1
    else:
        if result < 0:
            material_to_add = current_material + current_magic
            materials.append(material_to_add)
        else:
            materials.append(current_material + 15)

if ("Doll" in toys_crafted) and ("Wooden train" in toys_crafted) or \
        ("Teddy bear" in toys_crafted) and ("Bicycle" in toys_crafted):
# НЕ ТРЯБВА да е написано така if ("Doll" and "Train") in toys_crafted or ("Teddy bear" and "Bicycle") in toys_crafted:
    print(f"The presents are crafted! Merry Christmas!")
else:
    print(f"No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in reversed(materials))}")
if magic:
    print(f"Magic left: {', '.join(str(x) for x in magic)}")

if toys_crafted:
    for toy, quantity in sorted(toys_crafted.items()):
        print(f"{toy}: {quantity}")



# from collections import deque
#
# materials = [int(x) for x in input().split()]
# magic = deque((int(x) for x in input().split()))
#
# toys = {
#     150: "Doll",
#     250: "Wooden train",
#     300: "Teddy bear",
#     400: "Bicycle"
# }
#
# toys_crafted = {}
#
# while materials and magic:
#     current_material = materials[-1]
#     current_magic = magic[0]
#     result = current_material * current_magic
#     if current_material == 0:
#         materials.pop()
#     if current_magic == 0:
#         magic.popleft()
#     if result in toys:
#         crafted_toy = toys[result]
#         if crafted_toy not in toys_crafted:
#             toys_crafted[crafted_toy] = 1
#         else:
#             toys_crafted[crafted_toy] += 1
#         materials.pop()
#         magic.popleft()
#     else:
#         if result < 0:
#             sum_of_removed = current_magic + current_material
#             materials.pop()
#             magic.popleft()
#             materials.append(sum_of_removed)
#         elif result > 0:
#             magic.popleft()
#             materials[-1] = materials[-1] + 15
#
# if ("Doll" in toys_crafted) and ("Wooden train" in toys_crafted) or \
#         ("Teddy bear" in toys_crafted) and ("Bicycle" in toys_crafted):
#     print("The presents are crafted! Merry Christmas!")
# else:
#     print("No presents this Christmas!")
#
# if materials:
#     print(f"Materials left: {', '.join(str(x) for x in reversed(materials))}")
# if magic:
#     print(f"Magic left: {', '.join(str(x) for x in magic)}")
#
# for key, value in sorted(toys_crafted.items()):
#     print(f"{key}: {value}")


