command = input()

new_dict = {}

while command != "end":
    course, name = command.split(" : ")
    if course not in new_dict:
        new_dict[course] = []
        new_dict[course].append(name)
    elif course in new_dict:
        new_dict[course].append(name)
    command = input()

for course, name in sorted(new_dict.items(), key=lambda x: -len(x[1])):
    print(f"{course}: {len(name)}")
    for j in sorted(name):
        print(f"-- {j}")


