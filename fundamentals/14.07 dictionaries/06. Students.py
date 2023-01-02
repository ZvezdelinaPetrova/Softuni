data = input()

uni_dict = {}

while ":" in data:
    name, student_id, course = data.split(":")
    student_id = int(student_id)
    if name not in uni_dict:
        uni_dict[name] = {}
        uni_dict[name][student_id] = course
    data = input()

searched_word = data.split("_")
searched_word = " ".join(searched_word)
for key, value in uni_dict.items():
    for student_id, course in value.items():
        if course == searched_word:
            print(f"{key} - {student_id}")