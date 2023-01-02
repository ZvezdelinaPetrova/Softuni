num = int(input())
garage = {}

for _ in range(num):
    car, mileage, fuel_left = input().split('|')
    mileage = int(mileage)
    fuel_left = int(fuel_left)
    garage[car] = {'mileage': mileage, 'fuel_left': fuel_left}

command_line = input()
while not command_line == 'Stop':
    command_line = command_line.split(' : ')
    command = command_line[0]
    car = command_line[1]
    if command == 'Drive':
        distance = int(command_line[2])
        fuel = int(command_line[3])
        if garage[car]['fuel_left'] < fuel:
            print("Not enough fuel to make that ride")
        else:
            garage[car]['fuel_left'] -= fuel
            garage[car]['mileage'] += distance
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if garage[car]['mileage'] >= 100000:
                del garage[car]
                print(f"Time to sell the {car}!")
    elif command == 'Refuel':
        fuel = int(command_line[2])
        if garage[car]['fuel_left'] + fuel > 75:
            print(f"{car} refueled with {75 - garage[car]['fuel_left']} liters")
            garage[car]['fuel_left'] = 75
        else:
            garage[car]['fuel_left'] += fuel
            print(f"{car} refueled with {fuel} liters")
    elif command == 'Revert':
        km = int(command_line[2])
        garage[car]['mileage'] -= km
        if garage[car]['mileage'] < 10000:
            garage[car]['mileage'] = 10000
        else:
            print(f"{car} mileage decreased by {km} kilometers")
    command_line = input()

sorted_garage = sorted(garage.items(), key=lambda tkvp: (-tkvp[1]['mileage'], tkvp[0]))
for car, info in sorted_garage:
    print(f"{car} -> Mileage: {info['mileage']} kms, Fuel in the tank: {info['fuel_left']} lt.")