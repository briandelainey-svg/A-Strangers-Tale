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

#Arrays
items = {
    '[Short Sword]': 5,
    '[Goblin Club]': 10,
    '[Great Claw]': 20,
}
inventory = {}
stats = {
    'Str': 5,
    'Dex': 5,
    'Con': 5,
    'Int': 5,
    'Wis': 5,
    'Cha': 5
    }
choices = []
#Variables
name = 0
level = 0
state = 0
investigate = 0
exp = 0
#Functions
def slow_print(t): #makes text print slower
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.05) #change this to change speed
    print(' ') #dont touch this
def level():
    while True:
        
def fail():
    slow_print('Good job Dumbass')

#Game Save
print("""What save? (if file does not have a name, it's empty
1.
2.
3.
""")
choice = input(">>> ")

#Main
if name == 0:
    name = input('''What is your name, Hero?
>>> ''')
    
if state == 0:#Opening
    slow_print('You awaken at what seems to be home, yet remain unaware of where you are')
    slow_print('Next to the door you see a [Short Sword] hanging from a coat stand.')
    choice = input('''What do you do?
1. Grab the shortsword and leave.
2. Go back to bed
3. Investigate the cabin
>>> ''')
    choices.append(choice)
    if choice == '1':
        slow_print(' ')
    elif choce == '2':
        slow_print(' ')
    elif choice == '3':
        if investigate < 5 or investigate > 5:
            slow_print('You find Nothing')
            investigate += 1
        elif investigate == 5:
            slow_print('You find Nothing except for a small Cupboard behind the dresser with a [Glock]!')
            investigate += 1
    else:
        fail()
    state = 1
    
elif state == 1:#Cabin Exterior
    slow_print('Standing outside the cabin, you see a dense forest surounding you, with only a small deer path leeding outwards.')
elif state == 2:#Town
    slow_print('You enter town square, with the [Butcher], the [Blacksmith], and the [Library]')
elif state == 3:#Wandering Woods
    if Dragon == False:
        slow_print("You can't seem to enter the woods, as if some unseen force is preventing your movements")
        slow_print(f'"Come back when you are stronger, Hero [{name}]!"')
        state = 2
    elif Dragon == True:
        slow_print('The woods that once excluded you entry let you pass.')
elif state == 4:#castle
    slow_print('"Ahh. Another Foolish Hero. And who might you be?"')
