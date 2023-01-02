name = input()
password = input()
new_entry = input()

while new_entry != password:
    new_entry = input()
print(f"Welcome {name}!")
