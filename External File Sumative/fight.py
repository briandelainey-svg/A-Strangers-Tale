#####################################
## A Strangers Tale(combat)        ##
## External File Summative         ##
## Brian A. Delainey               ##
## Started - 3/19/2026             ##
## Finished -                      ##
#####################################

#imports
import random
import time
#Function
def combat(max_health, inventory, battle, weapons, armors, abilities, script, stats, health, gold, exp):
    #setup
    global outcome
    outcome = None
    ability = inventory['Ability']
    effect = abilities[ability]
    cooldown = 1
    damage = weapons[inventory['Weapon']]
    choice = None
    #Enemy type
    if battle == 1:
        enemy = 'Goblin'
        attacks = ["swings it's club"]
        hp = 60
        dmg = 3
        goldg = 8
        expg = 12
    elif battle == 2:
        enemy = 'Black Knight'
        attacks = ['Charges', 'Swings his sword', 'Bites your ankles off']
        hp = 90
        dmg = 5
        goldg = 12
        expg = 16
    #Main
    while hp > 0 and health > 0:
        
        #Reduces ability cooldown
        if cooldown > 0:
            cooldown -= 1
        elif cooldown == 0:
            cooldown -= 1
            print(f'{ability} is ready')
            time.sleep(.5)
        #Resets guard
        brace = False
        #Ensures health never exceeds max
        if health > max_health:
            health = max_health
        #Action
        print(f'You have {health} health remaining')
        time.sleep(.5)
        print('What do you do?')
        choice = input('''
    1. Attack
    2. Guard
    3. Ability
    4. Heal
    5. Run away
>>> ''')
        valid = True
        #Player attack
        if choice == '1':
            print(f'You attack the {enemy}!')
            hp -= damage
        #guard
        elif choice == '2':
            print(f'You brace yourself for an attack')
            brace = True
        #Ability
        elif choice == '3':
            #checks if you have an ability
            if ability!= 0:
                #Checks if you can use ability
                if cooldown <= 0:
                    cooldown = 3
                    print(f"You use {ability}!")
                    #Checks ability type
                    if ability == '[Cure wounds]' or ability == '[Meditative aura]' or ability == '[Holy word]':
                        #If healing type ability
                        print(f'You healed {effect} health')
                        health += effect
                        #if damage type ability
                    else:
                        hp -= effect
                #If you can't use ability
                else:
                    print('You cannot use that right now.')
                    print(f'{cooldown} cooldown')
                    #Player Heal
        elif choice == '4':
            print('What do you want to eat?')
            print(f"1. Apple {inventory['Food']['Apple']}")
            print(f"2. Bread {inventory['Food']['Bread']}")
            print(f"3. Jerkey {inventory['Food']['Jerkey']}")
            consume = input('>>> ')
            if consume == '1':
                if inventory['Food']['Apple'] >= 1:
                    consume = 'Apple'
                    health += 2
            elif consume == '2':
                if inventory['Food']['Bread'] >= 1:
                    consume = 'Bread'
                    health += 4
            elif consume == '3':
                if inventory['Food']['Jerkey'] >= 1:
                    consume = 'Jerkey'
                    health += 6
                    if inventory['Food'][consume] >= 1:
                        inventory['Food'][consume] -= 1
        #Escape
        elif choice == '5':
            #Checks if this is a scripted battle
            if script == True:
                print('You cannot run away')
            else:
                #Random chance to escape
                leave = random.randint(1, 4)
                if leave == 1:
                    print("You got away")
                    return health
                else:
                    print("You couldn't get away.")
        else:
            print('Invalid Input')
            valid = False
        #Enemy attack
        if hp > 0 and valid == True:
            attack = random.choice(attacks)
            print(f'The {enemy} {attack}!')
            health -= dmg
            if brace == True:
                health += 2
            time.sleep(.5)
            
    if health <= 0:
        outcome = False
        print('You died...')
        return health, gold, exp
        
    elif hp <= 0:
        outcome = True
        gold += goldg
        exp += expg
        print(f'You defeated the {enemy}!')
        return health, gold, exp
    
outcome = False
if __name__ == '__main__':
    print('Fight is the main')
    def bag(inventory):
        print(inventory)
    inventory = {'Weapon': '[Short Sword]',
                 'Armor': '[Iron armor]',
                 'Ability': '[Barrage]',
                 'Food': {
                     'Apple' : 0,
                     'Bread' : 5,
                     'Jerkey' : 0
                     }
                 }
    battle = 1
    weapons = {'[Short Sword]' :5}
    armors = {'[Iron armor]': 5}
    abilities = {'[Barrage]' :3}
    script = False
    stats = {
    'Str': 5,
    'Dex': 5,
    'Con': 5,
    'Int': 5,
    'Wis': 5,
    'Cha': 5
    }
    armor = armors[inventory['Armor']]
    max_health = stats['Con'] * 5 + armor
    health = max_health
    gold = 5
    combat(max_health, inventory, battle, weapons, armors, abilities, script, stats, gold)