day = input()
# ako e raboten -print working da
# ako e pochiven - print weekend
# ako e neshto drugo error da se printira

if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
    print("Working day")
elif day == "Saturday" or day == "Sunday":
    print("Weekend")
else:
    print("Error")

