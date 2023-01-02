target = input()
targeted_cities = {}

while not target == 'Sail':
    city, population, gold = target.split('||')
    population = int(population)
    gold = int(gold)
    if city not in targeted_cities:
        targeted_cities[city] = {'population': population, 'gold': gold}
    else:
        targeted_cities[city]['population'] += population
        targeted_cities[city]['gold'] += gold
    target = input()

command = input()
while not command == 'End':
    command = command.split('=>')
    event = command[0]
    city = command[1]
    if event == 'Plunder':
        people = int(command[2])
        gold = int(command[3])
        targeted_cities[city]['population'] -= people
        targeted_cities[city]['gold'] -= gold
        print(f"{city} plundered! {gold} gold stolen, {people} citizens killed.")
        if targeted_cities[city]['population'] <= 0 or targeted_cities[city]['gold'] <= 0:
            targeted_cities.pop(city)
            print(f"{city} has been wiped off the map!")
    elif event == 'Prosper':
        gold = int(command[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            targeted_cities[city]['gold'] += gold
            print(f"{gold} gold added to the city treasury. {city} now has {targeted_cities[city]['gold']} gold.")

    command = input()

if targeted_cities:
    sorted_cities = sorted(targeted_cities.items(), key=lambda tkvp: (-tkvp[1]['gold'], tkvp[0]))
    print(f"Ahoy, Captain! There are {len(sorted_cities)} wealthy settlements to go to:")
    for city, value in sorted_cities:
        print(f"{city} -> Population: {value['population']} citizens, Gold: {value['gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")