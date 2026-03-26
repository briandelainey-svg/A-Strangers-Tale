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



#Slow Print
def slow_print(t): #makes text print slower
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.05) #change this to change speed
    print(' ') #dont touch this
    
#Arrays
inventory = {'Weapon': 0,
             'Armor': None,
             'Ability': 0,
             'Food': {
                 'Apple': 0,
                 'Bread': 0,
                 'Jerkey': 0
                 }
             }#Current Held Items    
weapons = {0 : 0,
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
    'Brawler': {
        '[Barrage]': 3,
        '[Meditative aura]': 18,
        '[CHOMP!]': 14},
    'Wizard': {
        '[Firebolt]': 5,
        '[Cure wounds]': 8,
        '[AK47]': 23},
    'Warrior': {
        '[Power swing]': 8,
        '[Holy word]': 9,
        '[Throw]': weapons[inventory['Weapon']] * 3}
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
outcome = True
#Save data
save = [name, gold, event, level, stats, state, glock, style, exp, well, skull, max_health, health, choices ]
#Functions
    #Cabin Interior
def cabin(weapon, choices, state, health , max_health, outcome):
    global destination, glock
    if outcome == False:
        outcome = True
        slow_print("You wake up back at home. You could've sworn that was real... must've been a dream...")
        health = max_health
        print('You recovered all your health.')
    slow_print('Inside the cabin is mostly barren, but for a bed, an empty coatrack, and a solitary dresser')
    while state == 0:
        print(f'''What do you do?
1. Go to bed
2. Investigate the cabin
3. Leave the Cabin''')
        choice = input('''>>> ''')
        choices.append(choice)
        if choice  == 'b':
            bag(inventory, gold)
        if choice == '1':
            slow_print('You curl up in bed for a short rest')
            print('You recover all your health.')
            health = max_health
        elif choice == '2':
            if glock < 5 or glock > 5:
                slow_print('You find Nothing')
                glock += 1
            elif glock == 5:
                slow_print('You find Nothing except for a small Cupboard behind the dresser with a [Glock]!')
                print('You gained [Glock]')
                inventory['Weapon'] = '[Glock]'
                glock += 1
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
            bag(inventory, gold)
        elif choice == 'd':
            done(save)
        elif choice == '1':
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
                    bag(inventory, gold)
                elif choice == 'd':
                    done(save)
                elif choice == '1':
                    if skull == False:
                        slow_print('Looking through the woods, you find the deer skull is always 2 trees away. Always at the edge of your vision.')
                        skull = True
                        while True:
                            choice = input('''Do you continue, or return?
1. Continue onward
2. Return to the well
>>> ''')
                            choices.append(choice)
                            if choice  == 'b':
                                bag(inventory, gold)
                            elif choice == 'd':
                                done(save)
                            elif choice == '1':
                                slow_print('Walking through the woods, you follow the skulls gaze to a small clearing.')
                                slow_print('Inside the clearing, you see a ring of mushrooms around the perimeter.')
                                slow_print('Standing in the center is an old man.')
                                choice = input('''What do you do?
1. Attack the Man
2. Talk to the Man
>>> ''')
                                if choice == 'b':
                                    bag(inventory, gold)
                                elif choice == 'd':
                                    done(save)
                                elif choice == '1':
                                    slow_print('"A sorowful outcome. very well hero. Seek my home later."')
                                    fail()
                                    outcome = False
                                    destination = 0
                                    return
                                elif choice == '2':
                                    slow_print(f'"Hello, [{name}]. Welcome to my home. This land is full of many odd places as this."')
                                    slow_print('"You have dipped your toes into the [Wandering Woods]. Few may claim that, and even fewer may leave with there lives"')
                                    slow_print('"But you? I have plans for you. Unfortunatley, you are not privy to that information just yet."')
                                    if style == 'Warrior':
                                        print('You gained [Power swing]')
                                        ability = '[Power swing]'
                                    elif style == 'Mage':
                                        print('You gained [Firebolt]')
                                        ability = '[Firebolt]'
                                    elif style == 'Brawler':
                                        print('You gained [Barrage]!')
                                        ability = '[Barrage]'
                                    inventory['Ability'] = ability
                                    return
                    elif skull == True:
                        slow_print('As you try to enter the woods, a strange force keeps you out.')
                        slow_print('Best not to question it')
                    elif choice == '2':
                        break
                elif choice == '2':
                    if well == False:
                        slow_print('Looking down the well, you see what seems to be a body, only 2 feet down.')
                        slow_print('Pulling the corpse up you find it wearing a full set of armor')
                        if style == 'Warrior':
                            print('You gained [Iron armor]!')
                            armor = '[Iron armor]'
                        elif style == 'Mage':
                            print('You gained [Wizard robes]!')
                            armor = '[Wizard robes]'
                        elif style == 'Brawler':
                            print('You gained [Ninja suit]!')
                            armor = '[Ninja suit]'
                        inventory['Armor'] = armor
                        well = True
                    else:
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
def town(choices, state, gold):
    global event
    if event < 1:
        while True:
            slow_print('As you enter town, you find it all but deserted. All the people have disapeared.')
            slow_print("Your memory nags at the back of your head that somthing isn't right. The streets should be bustling with noon day shoppers.")
            slow_print('As you make to investigate, you spot a large cage full of people surrounded by goblinoid creatures with clubs.')
            slow_print('Walking towards them, you are suddonely accosted from behind.')
            script = True
            battle = 1
            combat(max_health, inventory, battle, weapons, armors, abilities, script, stats, done, bag)
            if outcome == True:
                event += 1
                slow_print('Killing the goblin, you make your way towards the cage')
                slow_print('Seeing there fallen comrad, the remaning goblins flee.')
                slow_print('"Thank you, Hero! What is your name?"')
                time.sleep(.5)
                slow_print(f'"{name}? Thank you, {name}!"')
                slow_print('"I am the village blacksmith. Please, come to my shop if you ever need armor or weapons!"')
                time.sleep(.5)
            else:
                fail()
                destination = 0
                return destination
        
    slow_print('You enter town square, with the [Butcher], the [Blacksmith], and the [Library]')
    while state == 2:
        choice = input('''Where do you go?
1.To the Butcher(Healing)
2.To the Blacksmith(Weapons)
3.To the Library(Abilities)
4.The Wandering woods
5.The Castle
6.The Cabin
>>> ''')
        
        choices.append(choice)
        if choice == 'b':
            bag(inventory, gold)
        elif choice == 'd':
            done(save)
        elif choice == '1':
            slow_print('"Welcome, Friend! What can I get for you?"')
            while True:
                print(f'Purse: [gold] gold')
                product = input('''
1.Apple(1 gold)
2.Bread(3 gold)
3.Jerkey(5 gold)
>>> ''')
                if product == '1':
                    product = 'Apple'
                    price = 1
                elif product == '2':
                    product = 'Bread'
                    price = 3
                elif product == '3':
                    produt = 'Jerkey'
                    price = 5
                amount = input('''How much?
>>> ''')
                total = price * amount
                if gold / total >= 1:
                    while amount > 0:
                        amount -= 1
                        gold -= price
                        inventory['Food'][product] += 1
                else:
                    slow_print('You dont have enough gold')
                print('"Anything else?"(y/n)')
                choice = input('>>> ')
                if choice == 'n':
                    break
                
        elif choice == '2':
            slow_print('')
            
        elif choice == '3':
            slow_print('"Welcome, To the library!"')
            slow_print('"Home to knowledge unbound, for a price of course!"')
            print(f'Purse: {gold} gold')
            if style == 'Brawler':
                slow_print('What do you want to learn?')
                print('(This will replace your current ability)')
                choice = input('''
1.Barrage(5 gold)
2.Meditative aura(10 gold)
3.CHOMP!(30 gold)
>>> ''')
                if choice == '1':
                    ability = '[Barrage]'
                    if inventory['Ability'] == ability:
                        print('You already have this ability')
                    else:
                        if gold >= 5:
                            print('You gained [Barrage]!')
                        else:
                            print("You don't have enough gold.")
                elif choice == '2':
                    ability = '[Meditative aura]'
                    if inventory['Ability'] == ability:
                        print('You already have this ability')
                    else:
                        if gold >= 5:
                            print('You gained [Meditative aura]!')
                        else:
                            print("You don't have enough gold.")
                elif choice == '3':
                    ability = '[CHOMP!]'
                    if inventory['Ability'] == ability:
                        print('You already have this ability')
                    else:
                        if gold >= 5:
                            print('You gained [CHOMP!]!')
                        else:
                            print("You don't have enough gold.")
                
            elif style == 'Wizard':
                slow_print('What do you want to learn?')
                print('(This will replace your current ability)')
                choice = input('''
1.Firebolt(5 gold)
2.Cure wounds(10 gold)
3.AK47(30 gold)
>>> ''')
                if choice == '1':
                    ability = '[Firebolt]'
                    if inventory['Ability'] == ability:
                        print('You already have this ability')
                    else:
                        if gold >= 5:
                            print('You gained [Firebolt]!')
                        else:
                            print("You don't have enough gold.")
                elif choice == '2':
                    ability = '[Cure wounds]'
                    if inventory['Ability'] == ability:
                        print('You already have this ability')
                    else:
                        if gold >= 5:
                            print('You gained [Cure wounds]!')
                        else:
                            print("You don't have enough gold.")
                elif choice == '3':
                    ability = '[AK47]'
                    if inventory['Ability'] == ability:
                        print('You already have this ability')
                    else:
                        if gold >= 5:
                            print('You gained [AK47]!')
                        else:
                            print("You don't have enough gold.")
                            
            elif style == 'Warrior':
                slow_print('What do you want to learn?')
                print('(This will replace your current ability)')
                choice = input('''
1.Power swing(5 gold)
2.Holy word(10 gold)
3.Throw(30 gold)
>>> ''')
                if choice == '1':
                    ability = '[Power swing]'
                    if inventory['Ability'] == ability:
                        print('You already have this ability')
                    else:
                        if gold >= 5:
                            print('You gained [Power swing]!')
                        else:
                            print("You don't have enough gold.")
                elif choice == '2':
                    ability = '[Holy word]'
                    if inventory['Ability'] == ability:
                        print('You already have this ability')
                    else:
                        if gold >= 5:
                            print('You gained [Holy word]!')
                        else:
                            print("You don't have enough gold.")
                elif choice == '3':
                    ability = '[Throw]'
                    if inventory['Ability'] == ability:
                        print('You already have this ability')
                    else:
                        if gold >= 5:
                            print('You gained [Throw]!')
                        else:
                            print("You don't have enough gold.")
            inventory['Ability'] = ability
            
                
        elif choice == '4':
            destination = 3
            return
        elif choice == '5':
            destination = 4
            return
        elif choice == '6':
            return
            destination = 1
            
            
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
def bag(inventory, gold):
    print(inventory)
    print(f'Purse: {gold} gold')
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
def done(save):
    with open(data, 'wb') as pickle_file:
        pickle.dump(save, pickle_file)
        destination = 12
        return destination
    
#Game Save
data = Path('data.pkl')#defines file path
print("Do you want to load a save?")
file = input("""1.Yes
2.No
>>> """)

if file == '1' or file == 'Yes':
    with open(data, 'rb') as pickle_file:#grabs all items from data.pkl
        save = pickle.load(pickle_file)

#Charecter Creator
if name == 0:
    name = input('''What is your name, Hero?
>>> ''')
    choices.append(name)
    slow_print(f'Hmmm. {name}. It shall do.')
    slow_print(f'So, {name}. How do you perfer to fight?')
    time.sleep(.5)
    while inventory['Weapon'] == 0:
        style = input('''
1. With a Sword(Str and Con)
2. With Staff and Spell(Int and Wis)
3. With my Fists(Dex and Lck)
>>> ''')
        choices.append(style)
        if style == '1':
            style = 'Warrior'
            slow_print('Very well, [Warrior]!')
            weapon = '[Short Sword]'
        elif style == '2':
            style = 'Mage'
            slow_print('As is only fitting, [Mage].')
            weapon = '[Staff]'
        elif style == '3':
            style = 'Brawler'
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
print('(Enter "b" at any time to open backpack)')
print('(Enter "d" at any time to close game)')
while True:
    if inventory['Armor'] != None:
        armor = armors[inventory['Armor']]
    else:
        armor = 0
    max_health = stats['Con'] * 5 + armor
    state = destination
    if state == 0:#Cabin Interior
        cabin(weapon, choices, state, health, max_health, outcome)
    elif state == 1:#Cabin Exterior
        cabin_ext(choices, well, skull, style, state)
    elif state == 2:#Town
        town(choices, state, gold)
    elif state == 3:#Wandering Woods
        woods(choices, state)
    elif state == 4:#Castle
        castle(choices, state)
    elif state == 12:#Game done
        print('Goodbye')
        sys.exit()