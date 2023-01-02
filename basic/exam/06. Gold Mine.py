destinations = int(input())
counter = 0
gold = 0

while destinations > counter:
    expected_gold = float(input())
    days_to_dig = int(input())
    gold = 0
    counter += 1
    for i in range(days_to_dig):
        new_gold = float(input())
        gold += new_gold
    average_gold = gold / days_to_dig
    if average_gold >= expected_gold:
        print(f"Good job! Average gold per day: {average_gold:.2f}.")
    elif average_gold < expected_gold:
        difference = abs(expected_gold - average_gold)
        print(f"You need {difference:.2f} gold.")

