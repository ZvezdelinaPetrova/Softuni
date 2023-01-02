money_needed = float(input())
money_in_hand = float(input())

counter = 0
days = 0
days_when_spending = 0
failed = False

while money_in_hand < money_needed:
    action = input()
    money = float(input())
    days += 1
    if action == "spend":
        days_when_spending += 1
        money_in_hand = money_in_hand - money
        if money_in_hand < 0:
            money_in_hand = 0
        if days_when_spending == 5:
            failed = True
            break
    elif action == "save":
        money_in_hand += money
        days_when_spending = 0

if failed:
    print("You can't save the money.")
    print(days)
else:
    print(f"You saved the money for {days} days.")


