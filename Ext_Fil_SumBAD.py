#####################################
## A Strangers Tale                ##
## External File Summative         ##
## Brian A. Delainey               ##
## Started - 3/11/2026             ##
## Finished -                      ##
#####################################

#Imports
import sys
import time
import random

#Slow Print
def slow_print(t): #makes text print slower
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.05) #change this to change speed
    print(' ') #dont touch this
    
#Arrays
weapons = {
    '[Fist Bindings]': 4,
    '[Gauntlets]': 8,
    '[Maulers]': 16,
    
    '[Staff]': 4,
    '[Crystal Wand]': 2,
    '[Dragons Breath Pikestaff]': 8,
    
    '[Short Sword]': 5,
    '[Goblin Club]': 10,
    '[Great Tooth]': 20
}#Weapon List
armors = {
    '[Ninja suit]': 3,
    '[Monks robes]': 6,
    '[Beasts pelt]': 14,
    
    '[Wizard robes]':2,
    '[Bloody regalia]': 4,
    '[Unholy cloak]': 4,
    
    '[Iron Armor]': 5,
    '[Giants hide]': 9,
    '[Dragonite plate]': 20
}#Armor types

classes = {
    'Brawler': {
        'Monk': 1,
        'Beast': 2
    },
    'Mage': {
        'Vampire': 1,
        'Necromancer': 2
    },
    'Warrior': {
        'Rampager': 1,
        'Knight': 2
    }
}#Classes and Subclasses

inventory = {'Weapon': 0,
             'Armor': 0
             }#Current Held Items

stats = {
    'Str': 5,
    'Dex': 5,
    'Con': 5,
    'Int': 5,
    'Wis': 5,
    'Cha': 5
}#Stats

choices = []#Choice list

#Variables
name = 0
level = 0
state = 0
investigate = 0
style = 0
exp = 0
well = False
max_health = 15
health = max_health

#Functions
    #Cabin Interior
def cabin(weapon, choices, state, health , max_health):
    slow_print('Inside the cabin is mostly barren, but for a bed, a coatrack, and a solitary dresser')
    while state == 0:
        print(f'''What do you do?
1. Go to bed
2. Investigate the cabin
3. Leave the Cabin''')
        choice = input('''>>> ''')
        choices.append(choice)
        if choice  == 'b':
            print(inventory)
        if choice == '1':
            slow_print('You curl up in bed for a short rest')
            print('You recover all your health.')
            health = max_health
        elif choice == '2':
            if investigate < 5 or investigate > 5:
                slow_print('You find Nothing')
                investigate += 1
            elif investigate == 5:
                slow_print('You find Nothing except for a small Cupboard behind the dresser with a [Glock]!')
                inventory['Weapon'] = '[Glock]'
                investigate += 1
        elif choice == '3':
            state = 1
            break
        else:
            fail()
        return state, health
    
    #Cabin Exterior
def cabin_ext(choices, well, style, state):
    slow_print('Standing outside your home, you see a dense forest surounding you, with only a small deer path leeding outwards.')
    choice = input('''What do you do?
1. Go inside
2. Explore
3. Follow the trail
>>> ''')
    choices.append(choice)
    if choice  == 'b':
        print(inventory)
    if choice == '1':
        state = 0
    elif choice == '2':
        slow_print('Walking around the cabin, you find a mostly empty yard. The only items of note being a deer skull staring through the trees,')
        slow_print('always following your gaze, and an old well, coated in blood.')
        while True:
            choice = input('''What do you do?
1. Explore the woods
2. Investigate the well
3. Go to the front of the Cabin
>>> ''')
            choices.append(choice)
            if choice  == 'b':
                print(inventory)
            if choice == '1':
                slow_print('Looking through the woods, you find the deer skull is always 2 trees away. Always at the edge of your vision.')
                while True:
                    choice = input('''Do you continue, or return?
1.Continue onward
2.Return to the well
>>> ''')
                    choices.append(choice)
                    if choice  == 'b':
                        print(inventory)
                    if choice == '1':
                        slow_print('')
                    elif choice == '2':
                        break
            elif choice == '2':
                if well == False:
                    well = True
                    slow_print('Looking down the well, you see what seems to be a body, only 2 feet down.')
                    slow_print('Pulling the corpse up you find it wearing a full set of armor')
                    if style == '1':
                        print('You gained [Iron armor]!')
                        armor = '[Iron armor]'
                    elif style == '2':
                        print('You gained [Wizards robes]!')
                        armor = '[Wizards robes]'
                    elif style == '3':
                        print('You gained [Ninja suit]!')
                        armor = '[Ninja suit]'
                    inventory['Armor'] = armor
                elif well == True:
                    slow_print('"You may not desecrate this body more, Hero!"')
            elif choice == '3':
                break
            else:
                fail()
    elif choice == '3':
        state = 2
    else:
        fail()
    return state

    #Town  
def town():
    slow_print('You enter town square, with the [Butcher], the [Blacksmith], and the [Library]')
    
    #The Woods
def woods(Dragon):
    if Dragon == False:
        slow_print("You can't seem to enter the woods, as if some unseen force is preventing your movements")
        slow_print(f'"Come back when you are stronger, Hero!"')
        state = 2
        
    elif Dragon == True:
        slow_print('The woods that once excluded you entry now let you pass.')

    #Castle
def castle():
        slow_print('"Ahh. Another Foolish Hero. And who might you be?"')

    #Level
def level(exp, level):
    slow_print(f'You are level {level}.')
    if exp == 100:
        exp = 0
        level += 1
        lvlup = input('''What stat do you wish to increase?
Str(Strength)
Dex(Dexterity)
Com(Constitution)
Int(Intelligence)
Wis(Wisdom)
Lck(Charisma)
>>> ''')
        choices.append(choice)
        if lvlup == '1' or lvlup == 'Strength':
            print('Strength has Been increased by 1!')
            stats['Str'] += 1
        elif lvlup == '2' or lvlup == 'Dexterity':
            print('Dexterity has Been increased by 1!')
            stats['Dex'] += 1
        elif lvlup == '3' or lvlup == 'Constitution':
            print('Constitution has Been increased by 1!')
            stats['Con'] += 1
        elif lvlup == '4' or lvlup == 'Intelligence':
            print('Intelligence has Been increased by 1!')
            stats['Int'] += 1
        elif lvlup == '5' or lvlup == 'Wisdom':
            print('Wisdom has Been increased by 1!')
            stats['Wis'] += 1
        elif lvlup == '6' or lvlup == 'Luck':
            print('Luck has Been increased by 1!')
            stats['Lck'] += 1
    else:
        tnl = 100 - exp
        slow_print(f'You need {tnl} more experience until next level up.')
    #Mess Up
def fail():
    slow_print('Good job Dumbass')

#Game Save
print("""What save? (if file does not have a name, it's empty
1.
2.
3. """)
choice = input(">>> ")
choices.append(choice)

#Main
if name == 0:
    name = input('''What is your name, Hero?
>>> ''')
    slow_print(f'Hmmm. {name}. It shall do.')
    slow_print(f'So, {name}. How do you perfer to fight?')
    time.sleep(.5)
    while inventory['Weapon'] == 0:
        style = input('''
1. With a Sword(Str and Con)
2. With Staff and Spell(Int and Wis)
3. With my Fists(Dex and Lck)
>>> ''')
        choices.append(choice)
        if style == '1':
            slow_print('Very well, [Warrior]!')
            weapon = '[Short Sword]'
        elif style == '2':
            slow_print('As is only fitting, [Mage].')
            weapon = '[Staff]'
        elif style == '3':
            slow_print('Daring are we, [Brawler]?')
            weapon = '[Fist Binding]'
        else:
            fail()
        inventory ['Weapon'] = weapon
    slow_print('You awaken at what seems to be home, yet remain unaware of where you are')
    slow_print(f'Next to the door you see a {weapon} and a backpack hanging from a coat stand.')
    slow_print(f'You equip the {weapon} and bag as you leave the Cabin.')
    state = 1
    
while True:
    max_health = stats['Con'] * 5
    if state == 0:#Cabin Interior
        cabin(weapon, choices, state, health, max_health)
    elif state == 1:#Cabin Exterior
        cabin_ext(choices, well, style, state)
    elif state == 2:#Town
        town(choices, state)
    elif state == 3:#Wandering Woods
        woods(choices, state)
    elif state == 4:#Castle
        castle(choices, state)
