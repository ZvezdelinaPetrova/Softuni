coaches = int(input())
command = input()
average_per_person = 0
number_of_presentations = 0
sum_evaluations = 0

while command != "Finish":
    name_of_presentation = command
    average_per_person = 0
    number_of_presentations += 1
    for i in range(coaches):
        new_evaluation = float(input())
        average_per_person += new_evaluation
    final_result_per_person = average_per_person / coaches
    sum_evaluations += final_result_per_person
    print(f"{name_of_presentation} - {final_result_per_person:.2f}.")
    command = input()
total = sum_evaluations / number_of_presentations
print(f"Student's final assessment is {total:.2f}.")