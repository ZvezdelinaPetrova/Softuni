text = input()

total = 0

for i in text:
    if i == "a":
        total = total + 1
    if i == "e":
        total = total + 2
    if i == "i":
        total = total + 3
    if i == "o":
        total = total + 4
    if i == "u":
        total = total + 5
print(total)

# moje da e s elif nyama da ima probem, to parvo pravi proverka na vsyaka bukva po otdelno