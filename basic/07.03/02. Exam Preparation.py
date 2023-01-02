bad_result = int(input())

counter_bad_results = 0
counter_positive_results = 0
total = 0
last_name = ""
failed = True
while counter_bad_results < bad_result:
    name = input()
    if name == "Enough":
        failed = False
        break
    last_name = name
    new_result = int(input())
    if new_result <= 4:
        counter_bad_results += 1
        total += new_result
    if new_result > 4:
        total += new_result
        counter_positive_results += 1

if failed:
    print(f"You need a break, {counter_bad_results} poor grades.")
else:
    average_grade = total / (counter_positive_results + counter_bad_results)
    print(f"Average score: {average_grade:.2f}")
    print(f"Number of problems: {counter_positive_results + counter_bad_results}")
    print(f"Last problem: {last_name}")