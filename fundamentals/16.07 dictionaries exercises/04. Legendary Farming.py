keys_dict = {"shards": 0, "fragments": 0, "motes": 0}
junk_dict = {}
break_the_cycle = False
legendary_item = ""
while True:
    if break_the_cycle:
        break
    data = input().split()
    for el in range(0, len(data), 2):
        key = data[el + 1].lower()
        value = int(data[el])
        if key in keys_dict:
            keys_dict[key] += value
            if keys_dict[key] >= 250:
                break_the_cycle = True
                keys_dict[key] -= 250
                legendary_item = key
                break
        elif key not in junk_dict:
            junk_dict[key] = value
        elif key in junk_dict:
            junk_dict[key] += value

if legendary_item == "motes":
    print("Dragonwrath obtained!")
elif legendary_item == "fragments":
    print("Valanyr obtained!")
elif legendary_item == "shards":
    print("Shadowmourne obtained!")

keys_dict = sorted(keys_dict.items(), key=lambda kvp: (-kvp[1], kvp[0]))

junk_dict = sorted(junk_dict.items(), key=lambda kvp: kvp[0])

for key, values in keys_dict:
    print(f"{key}: {values}")

for key, values in junk_dict:
    print(f"{key}: {values}")