import random

def combat(max_health):
    global health, inventory, battle, weapons, armors, abilities, script
    damage = weapons[inventory['Weapon']]
    if battle == 1:
        enemy = 'Goblin'
        attacks = ["The goblin swings it's club"]
        hp = 16
        dmg = 4
    while hp > 0 and health > 0:
        brace = False
        if health > max_health:
            health = max_health
        print('What do you do?')
        choice = input('''
1. Attack
2. Gaurd
3. Ability
4. Heal
5. Run away
>>> ''')
        if choice == '1':
            print(f'You attack the {enemy}!')
            hp -= damage

        elif choice == '2':
            print(f'You brace yourself for an attack')
            brace = True

        elif choice == '3':
            print(f"You use [{inventory['Abilitie']}!")
            #wip

        elif choice == '4':
            print('What do you want to eat?')
            print(f"1. Apple {inventory['Food']['Apple']}")
            print(f"2. Bread {inventory['Food']['Bread']}")
            print(f"3. Jerkey {inventory['Food']['Jerkey']}")
            consume = input('>>> ')
            if consume == '1':
                consume = 'Apple'
                health += 2
            elif consume == '2':
                consume = 'Bread'
                health += 4
            elif consume == '3':
                consume = 'Jerkey'
                health += 6
            inventory['Food'][consume] -= 1

        elif choice == '5':
            if script == True:
                print('You cannot run away')
            else:
                leave = random.randint(1, 4)
                if leave == 1:
                    print("You got away")
                    return health
                else:
                    print("You couldn't get away.")
        attack = random.choice(attacks)
        print(f'The {enemy} {attack}!')
        health -= dmg
        if brace == True:
            health += 2