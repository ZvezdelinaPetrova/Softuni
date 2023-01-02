from math import floor

cat_type = input()
gender = input()

years = 0

valid_cat = cat_type == "British Shorthair" or cat_type == "Siamese" or cat_type == "Persian" or cat_type == "Ragdoll" \
            or cat_type == "American Shorthair" or cat_type == "Siberian"

if not valid_cat:
    print(f"{cat_type} is invalid cat!")
elif gender == "m":
    if cat_type == "British Shorthair":
        years = (13 * 12) / 6
        print(f"{floor(years)} cat months")
    elif cat_type == "Siamese":
        years = (15 * 12) / 6
        print(f"{floor(years)} cat months")
    elif cat_type == "Persian":
        years = (14 * 12) / 6
        print(f"{floor(years)} cat months")
    elif cat_type == "Ragdoll":
        years = (16 * 12) / 6
        print(f"{floor(years)} cat months")
    elif cat_type == "American Shorthair":
        years = (12 * 12) / 6
        print(f"{floor(years)} cat months")
    elif cat_type == "Siberian":
        years = (11 * 12) / 6
        print(f"{floor(years)} cat months")
elif gender == "f":
    if cat_type == "British Shorthair":
        years = (14 * 12) / 6
        print(f"{floor(years)} cat months")
    elif cat_type == "Siamese":
        years = (16 * 12) / 6
        print(f"{floor(years)} cat months")
    elif cat_type == "Persian":
        years = (15 * 12) / 6
        print(f"{floor(years)} cat months")
    elif cat_type == "Ragdoll":
        years = (17 * 12) / 6
        print(f"{floor(years)} cat months")
    elif cat_type == "American Shorthair":
        years = (13 * 12) / 6
        print(f"{floor(years)} cat months")
    elif cat_type == "Siberian":
        years = (12 * 12) / 6
        print(f"{floor(years)} cat months")
