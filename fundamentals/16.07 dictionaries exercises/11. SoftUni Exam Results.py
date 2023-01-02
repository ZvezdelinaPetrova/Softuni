data = input()

new_dict = {}
language_dict = {}

while data != "exam finished":
    data = data.split("-")
    username = data[0]
    if data[1] == "banned":
        if username in new_dict:
            new_dict.pop(username)
    elif username not in new_dict:
        second_key = data[1]
        points = int(data[2])
        new_dict[username] = {}
        new_dict[username][second_key] = points
        if new_dict[username] == second_key:
            language_dict[second_key] += 1
        elif new_dict[username] != second_key:
            language_dict[second_key] = 1
    elif username in new_dict:
        m = 0
        last = list(new_dict[username].values())
        for value in last:
            m = int(value)
            break
        second_key = data[1]
        points = int(data[2])
        if m < points:
            new_dict[username][second_key] = points
        language_dict[second_key] += 1
        if new_dict[username] == second_key:
            language_dict[second_key] += 1
        elif new_dict[username] != second_key:
            language_dict[second_key] = 1
    data = input()

# for username, points in sorted(new_dict.items(), key=lambda x: (-(x[1]), x[0])):
#     print(f"{username} | {points}")
print("Submissions:")
for language, how_many in sorted(language_dict.items(), key=lambda x: (-(x[1]), x[0])):
    print(f"{language} - {how_many}")


