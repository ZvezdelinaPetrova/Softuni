n = int(input())

registrations = {}

for i in range(n):
    data = input().split()
    name = data[1]
    if data[0] == "register":
        if name not in registrations:
            registrations[name] = data[2]
            print(f"{name} registered {data[2]} successfully")
        elif name in registrations:
            print(f"ERROR: already registered with plate number {data[2]}")
    elif data[0] == "unregister":
        if name not in registrations:
            print(f"ERROR: user {name} not found")
        elif name in registrations:
            registrations.pop(name)
            print(f"{name} unregistered successfully")

for key, value in registrations.items():
    print(f"{key} => {value}")