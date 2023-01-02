from collections import deque


def check_for_success(res):
    if 100 <= res <= 199:
        return "Gemstone"
    elif 200 <= res <= 299:
        return "Porcelain Sculpture"
    elif 300 <= res <= 399:
        return "Gold"
    elif 400 <= res <= 499:
        return "Diamond Jewellery"


materials = deque(int(x) for x in input().split())  # last
magic = deque(int(x) for x in input().split())  # first
presents = {}
while materials and magic:
    current_material = materials.pop()
    current_magic = magic.popleft()
    result = current_material + current_magic

    if result < 100:
        if result % 2 == 0:
            new_result = (current_material * 2) + (current_magic * 3)
            if check_for_success(new_result):
                found = check_for_success(new_result)
                if found not in presents:
                    presents[found] = 1
                else:
                    presents[found] += 1
        elif result % 2 == 1:
            new_result = (current_material * 2) + (current_magic * 2)
            if check_for_success(new_result):
                found = check_for_success(new_result)
                if found not in presents:
                    presents[found] = 1
                else:
                    presents[found] += 1
    elif result > 499:
        new_result = result / 2
        if check_for_success(new_result):
            found = check_for_success(new_result)
            if found not in presents:
                presents[found] = 1
            else:
                presents[found] += 1
    else:
        if check_for_success(result):
            found = check_for_success(result)
            if found not in presents:
                presents[found] = 1
            else:
                presents[found] += 1


if "Gemstone" in presents and "Porcelain Sculpture" in presents or \
        "Gold" in presents and "Diamond Jewellery" in presents:
    print(f"The wedding presents are made!")
else:
    print(f"Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials)}")
if magic:
    print(f"Magic left: {', '.join(str(x) for x in magic)}")

for key, value in sorted(presents.items()):
    print(f"{key}: {value}")