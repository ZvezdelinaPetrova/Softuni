data = input()

new_dict = {}

while data != "End":
    name, id_of_student = data.split(" -> ")
    if name not in new_dict:
        new_dict[name] = []
        new_dict[name].append(id_of_student)
    else:
        if id_of_student not in new_dict[name]:
            new_dict[name].append(id_of_student)

    data = input()

new_dict = sorted(new_dict.items(), key=lambda kvp: kvp[0])
for key, value in new_dict:
    print(f"{key}")
    for i in value:
        print(f"-- {i}")

