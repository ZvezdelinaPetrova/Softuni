n = int(input())

first = ""
second = ""
third = ""


for i in range(n):
    first = chr(i + 97)
    for j in range(n):
        second = chr(j + 97)
        for x in range(n):
            third = chr(x + 97)
            print(f"{first}{second}{third}")




