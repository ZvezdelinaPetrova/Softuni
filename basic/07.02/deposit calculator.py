deposit = float(input())
months = int(input())
yearly_interest = float(input())
monthly_interest = deposit + months*((deposit * yearly_interest) / 100 / 12)
print(monthly_interest)

