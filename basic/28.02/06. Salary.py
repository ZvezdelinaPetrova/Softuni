n = int(input())
salary = int(input())

for i in range(1, n + 1):
    website = input()
    if salary <= 0:
        break
    if website == "Facebook":
        salary = salary - 150
    elif website == "Instagram":
        salary = salary - 100
    elif website == "Reddit":
        salary = salary - 50
if salary <= 0:
    print("You have lost your salary.")
else:
    print(salary)


