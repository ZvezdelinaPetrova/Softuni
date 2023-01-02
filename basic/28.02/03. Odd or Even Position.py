import sys
n = int(input())

odd_sum = 0
max_odd = - sys.maxsize
min_odd = sys.maxsize
even_sum = 0
max_even = - sys.maxsize
min_even = sys.maxsize

for i in range(1, n + 1):
    number = float(input())
    if i % 2 == 0:
        even_sum = even_sum + number
        if number > max_even:
            max_even = number
        if number < min_even:
            min_even = number
    elif i % 2 == 1:
        odd_sum = odd_sum + number
        if number > max_odd:
            max_odd = number
        if number < min_odd:
            min_odd = number

print(f"OddSum={odd_sum:.2f},")
if min_odd == sys.maxsize:
    print(f"OddMin=No,")
else:
    print(f"OddMin={min_odd:.2f},")
if max_odd == - sys.maxsize:
    print(f"OddMax=No,")
else:
    print(f"OddMax={max_odd:.2f},")

print(f"EvenSum={even_sum:.2f},")

if min_even == sys.maxsize:
    print(f"EvenMin=No,")
else:
    print(f"EvenMin={min_even:.2f},")
if max_even == - sys.maxsize:
    print(f"EvenMax=No")
else:
    print(f"EvenMax={max_even:.2f}")

