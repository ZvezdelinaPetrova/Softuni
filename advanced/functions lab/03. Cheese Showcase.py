def sorting_cheeses(**kwargs):
    test = sorted(kwargs.items(), key=lambda v: (-len(v[1]), v[0]))
    result = ''
    for k, value in test:
        result += f"{k}" + "\n"
        for el in sorted(value, reverse=True):
            result += f"{el}" + "\n"
    return result.strip()


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
