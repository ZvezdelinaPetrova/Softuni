meters = float(input())
all_without_discount = meters * 7.61
percentage = all_without_discount * 0.18
total_to_pay = all_without_discount - percentage
print(f"The final price is: {total_to_pay} lv.")
print(f"The discount is: {percentage} lv.")

