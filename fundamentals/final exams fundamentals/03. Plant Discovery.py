num = int(input())
collection = {}

for _ in range(num):
    plant, rarity = input().split('<->')
    collection[plant] = {}
    collection[plant]['rarity'] = int(rarity)
    collection[plant]['rating'] = []

command_line = input()

while not command_line == 'Exhibition':
    command, plant_info = command_line.split(': ')
    if command == 'Rate':
        plant, rating = plant_info.split(' - ')
        if plant not in collection:
            print('error')
        else:
            collection[plant]['rating'].append(int(rating))
    elif command == 'Update':
        plant, new_rarity = plant_info.split(' - ')
        if plant not in collection:
            print('error')
        else:
            collection[plant]['rarity'] = int(new_rarity)
    elif command == 'Reset':
        if plant_info not in collection:
            print('error')
        else:
            collection[plant_info]['rating'].clear()
    else:
        print('error')
    command_line = input()

print("Plants for the exhibition:")

sorted_collection = sorted(collection.items(), key=lambda kvp: (kvp[1]['rarity'], kvp[1]['rating']), reverse=True)

for plant in sorted_collection:
    if plant[1]['rating']:
        average_rating = sum(plant[1]['rating']) / len(plant[1]['rating'])
    else:
        average_rating = 0.00
    print(f"- {plant[0]}; Rarity: {plant[1]['rarity']}; Rating: {average_rating:.2f}")