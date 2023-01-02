people_happiness = [int(num) for num in input().split()]
improvement = int(input())

new_list = [el*improvement for el in people_happiness]
all_people = len(people_happiness)
average = sum(new_list) / len(people_happiness)

happy_count_filter = [num for num in new_list if num >= average]
happy_count = len(happy_count_filter)

if all_people / 2 > happy_count:
    print(f"Score: {happy_count}/{all_people}. Employees are not happy!")
else:
    print(f"Score: {happy_count}/{all_people}. Employees are happy!")
