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
import pickle
from pathlib import Path
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
    
    '[Staff]': 3,
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
abilities = { 
    '[Barrage]': 3,
    '[Meditative aura]': -18,
    '[CHOMP!]': 14,
    
    '[Firebolt]': 5,
    '[Cure wounds]': -8,
    '[AK47]': 23,
    
    '[Power swing]': 8,
    '[Holy word]': -9,
    '[Focus]': 0
}#Abilities
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

inventory = {'Weapon': None,
             'Armor': None,
             'Ability': None
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
state = 1
destination = 1
investigatec = 0
style = 0
exp = 0
well = False
skull = False
max_health = 15
health = max_health

#Functions
    #Cabin Interior
def cabin(weapon, choices, state, health , max_health):
    global destination
    slow_print('Inside the cabin is mostly barren, but for a bed, a coatrack, and a solitary dresser')
    while state == 0:
        print(f'''What do you do?
1. Go to bed
2. Investigate the cabin
3. Leave the Cabin''')
        choice = input('''>>> ''')
        choices.append(choice)
        if choice  == 'b':
            bag(inventory)
        if choice == '1':
            slow_print('You curl up in bed for a short rest')
            print('You recover all your health.')
            health = max_health
        elif choice == '2':
            if investigatec < 5 or investigatec > 5:
                slow_print('You find Nothing')
                investigatec += 1
            elif investigatec == 5:
                slow_print('You find Nothing except for a small Cupboard behind the dresser with a [Glock]!')
                inventory['Weapon'] = '[Glock]'
                investigatec += 1
        elif choice == '3':
            destination = 1
            return health
        else:
            fail()
    
    #Cabin Exterior
def cabin_ext(choices, well, skull, style, state):
    global destination
    slow_print('Standing outside your home, you see a dense forest surounding you, with only a small deer path leeding outwards.')
    while state == 1:
        choice = input('''What do you do?
1. Go inside
2. Explore
3. Follow the trail
>>> ''')
        choices.append(choice)
        if choice  == 'b':
            bag(inventory)
        if choice == '1':
            destination = 0
            return
        elif choice == '2':
            slow_print('Walking around the cabin, you find a mostly empty yard. The only items of note being a deer skull,')
            slow_print('staring deep into the woods, and an old well coated in blood.')
            while True:
                choice = input('''What do you do?
1. Explore the woods
2. Investigate the well
3. Go to the front of the Cabin
>>> ''')
                choices.append(choice)
                if choice  == 'b':
                    bag(inventory)
                if choice == '1':
                    if skull == False:
                        slow_print('Looking through the woods, you find the deer skull is always 2 trees away. Always at the edge of your vision.')
                        while True:
                            choice = input('''Do you continue, or return?
1. Continue onward
2. Return to the well
>>> ''')
                            choices.append(choice)
                            if choice  == 'b':
                                bag(inventory)
                            if choice == '1':
                                slow_print('Walking through the woods, you follow the skulls gaze to a small clearing.')
                                slow_print('Inside the clearing, you see a ring of mushrooms around ther perimeter. Standing in the center is an old man.')
                                choice = input('''What do you do?
1. Attack the Man
2. Talk to the Man
>>> ''')
                                if choice == '1':
                                    combat()
                                elif choice == '2':
                                    slow_print(f'"Hello, [{name}]. Welcome to my home. This land is full of many odd places as this."')
                                    slow_print('"You have dipped your toes into the [Wandering Woods]. Few may claim that, and even fewer may leave with there lives"')
                                    slow_print('"But you? I have plans for you. Unfortunatley, you are not privy to that information yet."')
                                    if style == '1':
                                        print('You gained [Power swing]')
                                        abilitie = '[Power swing]'
                                    elif style == '2':
                                        print('You gained [Firebolt]')
                                        abilitie = '[Firebolt]'
                                    elif style == '3':
                                        print('You gained [Barrage]!')
                                        abilitie = '[Barrage]'
                                    inventory['Ability'] = abilitie
                                    return
                    elif skull == True:
                        slow_print('As you try to enter the woods, a strange force keeps you out.')
                        slow_print('Best not to question it')
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
            destination = 2
            return
        else:
            fail()

    #Town  
def town(choices, state):
    slow_print('You enter town square, with the [Butcher], the [Blacksmith], and the [Library]')
    
    #The Woods
def woods(Dragon):
    global destination
    if Dragon == False:
        slow_print("You can't seem to enter the woods, as if some unseen force is preventing your movements")
        slow_print(f'"Come back when you are stronger, Hero!"')
        destination = 2
        
    elif Dragon == True:
        slow_print('The woods that once excluded you entry now let you pass.')

    #Castle
def castle():
        slow_print('"Ahh. Another Foolish Hero. And who might you be?"')

    #Backpack
def bag(inventory):
    print(inventory)
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
        choices.append(lvlup)
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
rep = 0
save = [inventory, state, name, style, level, investigatec, exp, stats, well, skull]
while rep < 3:
    rep += 1
    data = Path(f'{rep}.pkl')#defines file path
    if data.exists() and data.stat().st_size > 0:#checks if file already exists
        with open(data, 'rb') as pickle_file:#grabs all items from pkl file
            items = pickle.load(pickle_file)
    else:
        with open(f'{rep}.pkl', 'wb') as pickle_file:#creates .pkl file if it doesnt exist
            pickle.dump(name, pickle_file, protocol=pickle.HIGHEST_PROTOCOL)
        print(f'{rep}.{name} ')
        
print("What save? (if file does not have a name, it's empty)")
file = input(">>> ")


        
#Charecter Creator
if name == 0:
    name = input('''What is your name, Hero?
>>> ''')
    choices.append(name)
    slow_print(f'Hmmm. {name}. It shall do.')
    slow_print(f'So, {name}. How do you perfer to fight?')
    time.sleep(.5)
    while inventory['Weapon'] == None:
        style = input('''
1. With a Sword(Str and Con)
2. With Staff and Spell(Int and Wis)
3. With my Fists(Dex and Lck)
>>> ''')
        choices.append(style)
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
    
#Main
while True:
    max_health = stats['Con'] * 5
    if state == 0:#Cabin Interior
        cabin(weapon, choices, state, health, max_health)
        if destination == 1:
            state = 1
    elif state == 1:#Cabin Exterior
        cabin_ext(choices, well, skull, style, state)
        if destination == 0:
            state = 0
        elif destination == 2:
            state = 2
    elif state == 2:#Town
        town(choices, state)
        if destination == 1:
            state = 1
        elif destination == 3:
            state = 3
        elif destination == 4:
            state = 4
    elif state == 3:#Wandering Woods
        woods(choices, state)
        if destination == 2:
            state = 2
    elif state == 4:#Castle
        castle(choices, state)
