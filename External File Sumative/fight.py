#####################################
## A Strangers Tale(combat)        ##
## External File Summative         ##
## Brian A. Delainey               ##
## Started - 3/19/2026             ##
## Finished -                      ##
#####################################

#imports
import random

#Function
def combat(max_health):
    #setup
    global health, inventory, battle, weapons, armors, abilities, script, stats
    ability = inventory['Ability']
    effect = abilities[ability]
    cooldown = 0
    damage = weapons[inventory['Weapon']]
    #Enemy type
    if battle == 1:
        enemy = 'Goblin'
        attacks = ["The goblin swings it's club"]
        hp = 16
        dmg = 4
    #Main
    while hp > 0 and health > 0:
        
        #Reduces ability cooldown
        if cooldown > 0:
            cooldown -= 1
        elif cooldown == 0:
            print(f'{ability} is ready')
        #Resets gaurd
        brace = False
        #Ensures health never exceeds max
        if health > max_health:
            health = max_health
        #Enemy attack
        attack = random.choice(attacks)
        print(f'The {enemy} {attack}!')
        health -= dmg
        if brace == True:
            health += 2
        #Action
        print('What do you do?')
        choice = input('''
1. Attack
2. Gaurd
3. Ability
4. Heal
5. Run away
>>> ''')
        #Player attack
        if choice == '1':
            print(f'You attack the {enemy}!')
            hp -= damage
        #Gaurd
        elif choice == '2':
            print(f'You brace yourself for an attack')
            brace = True
        #Ability
        elif choice == '3':
            #checks if you have an ability
            if ability!= 0:
                #Checks if you can use ability
                if cooldown == 0:
                    cooldown = 3
                    print(f"You use {ability}!")
                    #Checks ability type
                    if ability == 'Cure wounds' or ability == 'Meditative aura' or ability == 'Holy word':
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
                consume = 'Apple'
                health += 2
            elif consume == '2':
                consume = 'Bread'
                health += 4
            elif consume == '3':
                consume = 'Jerkey'
                health += 6
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
    if health == 0:
        outcome = True
    elif hp == 0:
        outcome = False
    return outcome

if __name__ == '__main__':
    print('Fight is the main')