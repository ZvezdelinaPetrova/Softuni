version = [el for el in input().split(".")]
version_as_number = int("".join(version)) + 1
version_as_string = str(version_as_number)
print(".".join(version_as_string))