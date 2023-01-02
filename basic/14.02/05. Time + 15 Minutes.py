hours = int(input())
minutes = int(input())

minutes = minutes + 15
hours = hours + minutes // 60   # taka deli celochisleno delene

minutes = minutes % 60  #ostatak e tova
if hours > 23:
    hours = hours - 24
if minutes <= 9:
    print(f"{hours}:0{minutes}")
else:
    print(f"{hours}:{minutes}")

#drug varant za minuti da ima 0-la otpred e da napishem {minutes:0>2d}