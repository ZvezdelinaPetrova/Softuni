def grocery_store(**kwargs):
    result = ""
    new_dict = {}
    for key, value in kwargs.items():
        new_dict[key] = value
    tested = sorted(new_dict.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    for k, v in tested:
        result += f"{k}: {v}" + "\n"
    return result.strip()


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))


print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))
