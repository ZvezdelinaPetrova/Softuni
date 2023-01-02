data = input().split(", ")

for username in data:
    if 3 <= len(username) <= 16:
        invalid_symbols = [el for el in username if not el.isdigit() and not el.isalpha() and not el == "-" and not el == "_"]
        if len(invalid_symbols) == 0:
            print(username)

