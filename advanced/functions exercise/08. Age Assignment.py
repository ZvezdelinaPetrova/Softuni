def age_assignment(*args, **kwargs):
    result = ""
    new_dict = {}
    for key, value in kwargs.items():
        for el in args:
            first = el[0]
            if first == key:
                new_dict[el] = value
    for key, value in sorted(new_dict.items()):
        result += f"{key} is {value} years old." + "\n"
    return result.strip()


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))

