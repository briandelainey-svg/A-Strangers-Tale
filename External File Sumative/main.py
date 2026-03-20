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
from fight import combat
from locations import cabin, cabin_ext, town, woods, castle

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
    '[Meditative aura]': 18,
    '[CHOMP!]': 14,
    
    '[Firebolt]': 5,
    '[Cure wounds]': 8,
    '[AK47]': 23,
    
    '[Power swing]': 8,
    '[Holy word]': 9,
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
             'Ability': None,
             'Food': {
                 'Apple': 0,
                 'Bread': 0,
                 'Jerkey': 0
                 }
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
gold = 0
event = 0
level = 0
state = 1
destination = 1
glock = 0
style = 0
exp = 0
well = False
skull = False
max_health = 15
health = max_health
#Save data
save = [name, gold, event, level, stats, state, glock, style, exp, well, skull, max_health, health, choices ]
#Functions
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
    data = Path(f'{file}.pkl')#defines file path
if data.exists() and data.stat().st_size > 0:#checks if file already exists
    with open(data, 'rb') as pickle_file:#grabs all items from pkl file
        items = pickle.load(pickle_file)
else:
    with open('1.pkl', 'wb') as pickle_file:#creates .pkl file if it doesnt exist
        pickle.dump(items, pickle_file, protocol=pickle.HIGHEST_PROTOCOL)
        
print("""What save? (if file does not have a name, it's empty
1.
2.
3. """)
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
    slow_print(f'Next to the door you see a {weapon} and a backpack full of bread hanging from a coat stand.')
    slow_print(f'You equip the {weapon} and bag as you leave the Cabin.')
    inventory ['Food']['Bread'] += 5
    
#Main
while True:
    armor = armors[inventory['Armor']]
    max_health = stats['Con'] * 5 + armor
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
