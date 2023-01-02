hour = int(input())
day = input()

# ot 10-18  bachka
# poneldenik do sabota bachka else nedelya ne bachka(elif)

if 10 <= hour <= 18:
    if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday"\
            or day == "Saturday":
        print("open")
    elif day == "Sunday":
        print("closed")
else:
    print("closed")

#ima i takova reshenie

# if 10 <= hour <= 18 and day != "Sunday":
#    print("open")
# else:
#    print("closed")
