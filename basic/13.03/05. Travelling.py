destination = input()
while destination != "End":
    budget = float(input())
    counter = 0
    while counter < budget:
        new_money = float(input())
        counter += new_money
        if counter >= budget:
            print(f"Going to {destination}!")
    destination = input()



