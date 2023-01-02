from math import floor

income = float(input())
evaluation = float(input())
salary = float(input())

social_scholarship = salary * 0.35   # int(salary * 0.35) taka se vzima dori da e 2.57657 maha se vsichko sled 2
excellent_scholarship = evaluation * 25

if evaluation >= 5.5:
    if income > salary:
        print(f"You get a scholarship for excellent results {floor(excellent_scholarship)} BGN")
    else:
        if excellent_scholarship >= social_scholarship:
            print(f"You get a scholarship for excellent results {floor(excellent_scholarship)} BGN")
        else:
            print(f"You get a Social scholarship {floor(social_scholarship)} BGN")

elif evaluation > 4.5:
    if income < salary:
        print(f"You get a Social scholarship {floor(social_scholarship)} BGN")
    else:
        print("You cannot get a scholarship!")
else:
    print("You cannot get a scholarship!")




