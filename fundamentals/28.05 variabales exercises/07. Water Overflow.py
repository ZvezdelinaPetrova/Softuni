lines = int(input())

capacity = 255

counter = 0

for i in range(lines):
    new_liters = int(input())
    counter += new_liters
    if counter > capacity:
        print("Insufficient capacity!")
        counter -= abs(new_liters)
print(counter)