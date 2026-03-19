import random
def combat(max_health):
    global health, inventory, battle, weapons, armors, abilities
    damage = weapons[inventory['Weapon']]
    if battle == 1:
        enemy = goblin
        attacks = ["The goblin swings it's club"]
        hp = 16
    
    