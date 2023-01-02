# import re
#
# n = int(input())
#
# pattern = r"((\$(?P<tag>[A-Z][a-z]+)\$)\:\s\[(?P<first>[0-9]+)\]\|\[(?P<second>[0-9]+)\]\|\[(?P<third>[0-9]+)\]\|)"
# pattern_1 = r"((\%(?P<tag>[A-Z][a-z]+)\%)\:\s\[(?P<first>[0-9]+)\]\|\[(?P<second>[0-9]+)\]\|\[(?P<third>[0-9]+)\]\|)"
# for _ in range(n):
#     text = input()
#     my = [i for i in re.findall(pattern, text)]
#     two = [i for i in re.findall(pattern_1, text)]
#     if my:
#         pass
#     elif two:
#         pass
#     else:
#         print("Valid message not found!")
import re
lines_count = int(input())
pattern = r"(?P<del>\*|@)(?P<first>([A-Z][a-z]{2,}))(?P=del):\s(?P<second>(\[[A-Za-z]\]\|){3}$)"

for _ in range(lines_count):
    message = input()
    message = re.finditer(pattern, message)
    valid = None
    for g in message:
        first = g.groupdict()['first']
        second = g.groupdict()['second']
        new_second = []
        for i in range(len(second)):
            if second[i].isalpha():
                new_second.append(str(ord(second[i])))
        valid = first + ": " + " ".join(new_second)

    if valid:
        print(valid)
    else:
        print(f"Valid message not found!")