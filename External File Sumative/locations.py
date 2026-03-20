#####################################
## A Strangers Tale(locations)     ##
## External File Summative         ##
## Brian A. Delainey               ##
## Started - 3/20/2026             ##
## Finished -                      ##
#####################################
#Imports
from fight import combat
#Functions
    #Cabin Interior
def cabin(weapon, choices, state, health , max_health):
    global destination
    slow_print('Inside the cabin is mostly barren, but for a bed, an empty coatrack, and a solitary dresser')
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
            if glock < 5 or glock > 5:
                slow_print('You find Nothing')
                glock += 1
            elif glock == 5:
                slow_print('You find Nothing except for a small Cupboard behind the dresser with a [Glock]!')
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
def town(choices, state, gold):
    global event
    if event < 1:
        event += 1
        slow_print('As you enter town, you find it all but deserted. All the people have disapeared.')
        slow_print("Your memory nags at the back of your head that somthing isn't right. The streets should be bustling with noon day shoppers.")
        slow_print('As you make to investigate, you spot a large cage full of people surrounded by goblinoid creatures with clubs.')
        slow_print('Walking towards them, you are suddonely accosted from behind.')
        script = True
        battle = 1
        combat(max_health)
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
