num = int(input())
heroes = {}

for _ in range(num):
    hero, hit_p, mana_p = input().split()
    hit_p = int(hit_p)
    mana_p = int(mana_p)
    heroes[hero] = {'hit_p': hit_p, 'mana_p': mana_p}

command_line = input()
while not command_line == 'End':
    command_line = command_line.split(' - ')
    command = command_line[0]
    hero = command_line[1]
    if command == 'CastSpell':
        mana_needed = int(command_line[2])
        spell = command_line[3]
        if mana_needed <= heroes[hero]['mana_p']:
            heroes[hero]['mana_p'] -= mana_needed
            print(f"{hero} has successfully cast {spell} and now has {heroes[hero]['mana_p']} MP!")
        else:
            print(f"{hero} does not have enough MP to cast {spell}!")
    elif command == 'TakeDamage':
        damage = int(command_line[2])
        attacker = command_line[3]
        heroes[hero]['hit_p'] -= damage
        if heroes[hero]['hit_p'] > 0:
            print(f"{hero} was hit for {damage} HP by {attacker} and now has {heroes[hero]['hit_p']} HP left!")
        else:
            print(f"{hero} has been killed by {attacker}!")
            del heroes[hero]
    elif command == 'Recharge':
        amount = int(command_line[2])
        if heroes[hero]['mana_p'] + amount > 200:
            print(f"{hero} recharged for {200 - heroes[hero]['mana_p']} MP!")
            heroes[hero]['mana_p'] = 200
        else:
            heroes[hero]['mana_p'] += amount
            print(f"{hero} recharged for {amount} MP!")
    elif command == 'Heal':
        amount = int(command_line[2])
        if heroes[hero]['hit_p'] + amount > 100:
            print(f"{hero} healed for {100 - heroes[hero]['hit_p']} HP!")
            heroes[hero]['hit_p'] = 100
        else:
            heroes[hero]['hit_p'] += amount
            print(f"{hero} healed for {amount} HP!")
    command_line = input()

heroes_left = sorted(heroes.items(), key=lambda tkvp: (-tkvp[1]['hit_p'], tkvp[0]))
if heroes_left:
    for hero, info in heroes_left:
        print(f"{hero}")
        print(f"  HP: {info['hit_p']}")
        print(f"  MP: {info['mana_p']}")