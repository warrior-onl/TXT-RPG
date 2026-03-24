# OF NOBLE LIGHT - txt_rpg

import os
import random

# Text colors
RESET  = '\033[0m'
BOLD   = '\033[1m'
YELLOW = '\033[93m'
CYAN   = '\033[96m'
WHITE  = '\033[97m'

# Element colors
EARTH = '\033[1m\033[43m\033[30m'
AIR   = '\033[1m\033[107m\033[30m'
FIRE  = '\033[1m\033[101m\033[30m'
WATER = '\033[1m\033[44m\033[30m'
# Refined element colors
STONE = '\033[1m\033[100m\033[97m'
STORM = '\033[1m\033[40m\033[97m'
MAGMA = '\033[1m\033[41m\033[97m'
ICE   = '\033[1m\033[106m\033[97m'
# Evolved element colors
NATURE   = '\033[1m\033[42m\033[97m'
ELECTRIC = '\033[1m\033[103m\033[97m'
PLASMA   = '\033[1m\033[104m\033[97m'
AETHER   = '\033[1m\033[45m\033[97m'

# Class stat modifiers
class_mods = {
    'Warrior':   {'ATK': 2, 'DEF': 2, 'ETK': 0, 'EDF': 0, 'EVN': 1, 'SPD': 0, 'AFT': 0},
    'Warden':    {'ATK': 2, 'DEF': 3, 'ETK': 0, 'EDF': 3, 'EVN': 2, 'SPD': 0, 'AFT': 0},
    'Arbiter':   {'ATK': 1, 'DEF': 1, 'ETK': 4, 'EDF': 1, 'EVN': 2, 'SPD': 1, 'AFT': 0},
    'Caster':    {'ATK': 2, 'DEF': 1, 'ETK': 1, 'EDF': 0, 'EVN': 0, 'SPD': 1, 'AFT': 0},
    'Ranger':    {'ATK': 2, 'DEF': 1, 'ETK': 1, 'EDF': 0, 'EVN': 2, 'SPD': 4, 'AFT': 0},              
    'Channeler': {'ATK': 3, 'DEF': 1, 'ETK': 3, 'EDF': 1, 'EVN': 0, 'SPD': 2, 'AFT': 0},
    'Sage':      {'ATK': 0, 'DEF': 0, 'ETK': 1, 'EDF': 1, 'EVN': 1, 'SPD': 1, 'AFT': 1},
    'Shaman':    {'ATK': 0, 'DEF': 2, 'ETK': 1, 'EDF': 2, 'EVN': 2, 'SPD': 1, 'AFT': 2},
    'Primal':    {'ATK': 3, 'DEF': 0, 'ETK': 3, 'EDF': 1, 'EVN': 1, 'SPD': 1, 'AFT': 1},
    'Magi':      {'ATK': 0, 'DEF': 0, 'ETK': 2, 'EDF': 2, 'EVN': 0, 'SPD': 0, 'AFT': 1},
    'Alchemist': {'ATK': 1, 'DEF': 0, 'ETK': 4, 'EDF': 0, 'EVN': 1, 'SPD': 2, 'AFT': 3},
    'Druid':     {'ATK': 0, 'DEF': 3, 'ETK': 0, 'EDF': 4, 'EVN': 1, 'SPD': 0, 'AFT': 2},
}
# Base class list
base_classes = ['Warrior', 'Caster', 'Sage', 'Magi']
# Class mastery paths
mastery_paths = {
    'Warrior': ['Warden', 'Arbiter'],
    'Caster':  ['Ranger', 'Channeler'],
    'Sage':    ['Shaman', 'Primal'],
    'Magi':    ['Alchemist', 'Druid'],
}

# Element stat modifiers
element_mods = {
    'Earth':    {'HP': 5, 'ATK': 1, 'DEF': 3, 'ETK': 1, 'EDF': 2, 'EVN': -1, 'SPD': -1, 'AFT': 0},
    'Stone':    {'HP': 6, 'ATK': 0, 'DEF': 4, 'ETK': 0, 'EDF': 4, 'EVN': -2, 'SPD': -2, 'AFT': 0},
    'Nature':   {'HP': 8, 'ATK': -3, 'DEF': 1, 'ETK': -3, 'EDF': 1, 'EVN': 2, 'SPD': -2,'AFT': 6},
    'Air':      {'HP': 2, 'ATK': -1, 'DEF': -1, 'ETK': 2, 'EDF': 1, 'EVN': 3, 'SPD': 4, 'AFT': 0},
    'Storm':    {'HP': 2, 'ATK': -1, 'DEF': -1, 'ETK': 2, 'EDF': 2, 'EVN': 2, 'SPD': 0, 'AFT': 4},
    'Electric': {'HP': 0, 'ATK': 3, 'DEF': -2, 'ETK': 3, 'EDF': -2, 'EVN': 5, 'SPD': 3, 'AFT': 0},
    'Fire':     {'HP': -2, 'ATK': 4, 'DEF': 0, 'ETK': 4, 'EDF': 0, 'EVN': 2, 'SPD': 2, 'AFT': 0},
    'Magma':    {'HP': 2, 'ATK': 1, 'DEF': 3, 'ETK': 1, 'EDF': 3, 'EVN': 0, 'SPD': -2, 'AFT': 2},
    'Plasma':   {'HP': -4, 'ATK': 7, 'DEF': -3, 'ETK': 7, 'EDF': -3, 'EVN': 1, 'SPD': 5, 'AFT': 0},
    'Water':    {'HP': 6, 'ATK': 0, 'DEF': 1, 'ETK': 0, 'EDF': 1, 'EVN': 1, 'SPD': 0, 'AFT': 1},
    'Ice':      {'HP': -2, 'ATK': 2, 'DEF': -3, 'ETK': 4, 'EDF': 2, 'EVN': 2, 'SPD': 3, 'AFT': 2},
    'Aether':   {'HP': 2, 'ATK': 0, 'DEF': 0, 'ETK': 0, 'EDF': 0, 'EVN': 4, 'SPD': 0, 'AFT': 4},
}
# Element progression trees
element_trees = {
    'Earth': ['Earth', 'Stone', 'Nature'],
    'Air':   ['Air', 'Storm', 'Electric'],
    'Fire':  ['Fire', 'Magma', 'Plasma'],
    'Water': ['Water', 'Ice', 'Aether'],
}

# Move power Values
move_power = {
    'basic': 60,
    'A': 80,
    'B': 100,
    'C': 120,
    'D': 145,
    'E': 170,
}

def create_stats(player_class, element):
    base = 15
    c = class_mods[player_class]
    e = element_mods[element]
    stats = {
        'HP':  base + e['HP'],
        'ATK': base + c['ATK'] + e['ATK'],
        'DEF': base + c['DEF'] + e['DEF'],
        'ETK': base + c['ETK'] + e['ETK'],
        'EDF': base + c['EDF'] + e['EDF'],
        'EVN': base + c['EVN'] + e['EVN'],
        'SPD': base + c['SPD'] + e['SPD'],
        'AFT': base + c['AFT'] + e['AFT'],
    }
    return stats

def show_stats(name, player_class, element_1, element_2, level, stats, player_xp):
    print('')
    print(YELLOW + BOLD + '--- CHARACTER ---' + RESET)
    print('Name:    ' + name)
    print('Class:   ' + player_class)
    print('Element: ' + element_1)
    if element_2 != 'None':
        print('Slot 2: ' + element_2)
    print('Level:   ' + level)
    xp_needed = int(level) * 25 + 10
    print('XP:      ' + str(player_xp) + '/' + str(xp_needed))
    print('')
    print(YELLOW + BOLD + '--- STATS ---' + RESET)
    print('HP:  ' + str(stats['HP']))
    print('ATK: ' + str(stats['ATK']))
    print('DEF: ' + str(stats['DEF']))
    print('ETK: ' + str(stats['ETK']))
    print('EDF: ' + str(stats['EDF']))
    print('EVN: ' + str(stats['EVN']))
    print('SPD: ' + str(stats['SPD']))
    print('AFT: ' + str(stats['AFT']))
    print('')

def game_hub(name, player_class, player_element, player_element_2, player_level, stats, player_xp):
    while True:
        print('')
        print(YELLOW + BOLD + '--- HOME BASE ---' + RESET)
        print('')
        print(CYAN + ' 1. Enter Region' + RESET)
        print(CYAN + ' 2. View Character' + RESET)
        print(CYAN + ' 3. Save and Quit' + RESET)
        print('')
        hub_choice = input('What would you like to do? ')

        if hub_choice == '1':
            region = select_region()
            if region is None:
                continue
            difficulty = select_difficulty()
            if difficulty is None:
                continue
            print('')
            print('Entering ' + region + ' Region on ' + difficulty + ' difficulty...')
            run_ended = False
            for path in range(1, 5):
                result = run_path(path, region, difficulty, name, player_class, player_element, stats, player_level)
                if result in ['lost', 'fled']:
                    run_ended = True
                    break
            if not run_ended:
                print('')
                print('A powerful presence blocks your path...')
                print('[Boss battle placeholder]')
                print('')
                print('You completed the ' + region + ' Region!')
        elif hub_choice == '2':
            show_stats(name, player_class, player_element, player_element_2, player_level, stats, player_xp)
        elif hub_choice == '3':
            with open('txt_rpg/save.txt', 'w') as file:
                file.write(name + '\n')
                file.write(player_class + '\n')
                file.write(player_element + '\n')
                file.write(player_element_2 + '\n')
                file.write(player_level + '\n')
                file.write(str(player_xp) + '\n')
            print('Game saved. Goodbye, ' + name + '.')
            break
        else:
            print('Invalid choice.')

def select_region():
    while True:
        print('')
        print(YELLOW + BOLD + '--- SELECT REGION ---' + RESET)
        print('')
        print(' 1. ' + EARTH + ' EARTH REGION ' + RESET + ' - grasslands, forests, deserts')
        print(' 2. ' + AIR + ' AIR REGION ' + RESET + ' - levitating islands, mountains')
        print(' 3. ' + FIRE + ' FIRE REGION ' + RESET + ' - desert, volcanic terrain')
        print(' 4. ' + WATER + ' WATER REGION ' + RESET + ' - coasts, northern mountains, inland lakes')
        print(CYAN + ' 5. Back' + RESET)
        print('')
        region_choice = input('Pick a region: ')

        if region_choice == '1':
            return 'Earth'
        elif region_choice == '2':
            return 'Air'
        elif region_choice == '3':
            return 'Fire'
        elif region_choice == '4':
            return 'Water'
        elif region_choice == '5':
            return None
        else:
            print('Invalid choice.')

def select_difficulty():
    while True:
        print('')
        print(YELLOW + BOLD + '--- SELECT DIFFICULTY ---' + RESET)
        print('')
        print(CYAN + ' 1. Novice' + RESET + ' - weaker enemies, base elements only')
        print(CYAN + ' 2. Adept' + RESET + ' - matched enemies, base + refined elements')
        print(CYAN + ' 3. Expert' + RESET + ' - stronger enemies, all elements')
        print(CYAN + ' 4. Back' + RESET)
        print('')
        diff_choice = input('Pick a difficulty: ')

        if diff_choice == '1':
            return 'Novice'
        elif diff_choice == '2':
            return 'Adept'
        elif diff_choice == '3':
            return 'Expert'
        elif diff_choice == '4':
            return None
        else:
            print('Invalid choice.')

def run_path(path_number, region, difficulty, name, player_class, player_element, stats, player_level):
    print('')
    print(YELLOW + BOLD + '--- Path ' + str(path_number) + ' of 4 ---' + RESET)
    print('')
    print('You come to a fork in the road.')
    print('')
    print(CYAN + ' 1. Left' + RESET)
    print(CYAN + ' 2. Right' + RESET)
    print('')
    while True:
        fork = input('Which way? ')
        if fork in ['1', '2']:
            break
        print('Invalid choice.')

    guaranteed = random.randint(1, 3)
    had_random_battle = False

    for stop in range(1, 4):
        print('')
        print('--- Stop ' + str(stop) + ' of 3 ---')

        if stop == guaranteed:
            encounter = 'battle'
        else:
            roll = random.randint(1, 100)
            if had_random_battle:
                if roll <= 10:
                    encounter = 'battle'
                elif roll <= 55:
                    encounter = 'nothing'
                elif roll <= 80:
                    encounter = 'traveler'
                else:
                    encounter = 'loot'
            else:
                if roll <= 35:
                    encounter = 'battle'
                elif roll <= 70:
                    encounter = 'nothing'
                elif roll <= 90:
                    encounter = 'traveler'
                else:
                    encounter = 'loot'

        if encounter == 'battle':
            print('The Dim emerge from the shadows!')
            result = battle(name, stats, region, difficulty, player_level)
            if result == False:
                print('Your journey ends here...')
                return 'lost'
            elif result == 'fled':
                print('You retreat back to base.')
                return 'fled'
            had_random_battle = True
        elif encounter == 'nothing':
            print('The path is quiet. You press forward.')
        elif encounter == 'traveler':
            print('You spot a traveler on the road ahead.')
            print('[Traveler placeholder]')
        elif encounter == 'loot':
            print('You spot something glinting off the path.')
            print('[Loot placeholder]')

def create_enemy(region, difficulty, player_level):
    level = int(player_level)
    if difficulty == 'Novice':
        enemy_level = max(1, int(level * 0.8))
    elif difficulty == 'Adept':
        enemy_level = level
    else:
        enemy_level = max(1, int(level * 1.25))
    
    enemy_class = random.choice(base_classes)
    if enemy_level >=30:
        enemy_class = random.choice(mastery_paths[enemy_class])

    enemy_element = region
    if enemy_level >= 15 and difficulty != 'Novice':
        tree = element_trees[region]
        enemy_element = tree[1]
    if enemy_level >= 35 and difficulty == 'Expert':
        tree = element_trees[region]
        enemy_element = tree[2]

    enemy_element_2 = 'None'
    if enemy_level >= 15:
        other_trees = [t for t in element_trees if t != region]
        second_tree = random.choice(other_trees)
        if enemy_level >= 35 and difficulty == 'Expert':
            enemy_element_2 = element_trees[second_tree][2]
        elif enemy_level >= 15 and difficulty != 'Novice':
            enemy_element_2 = element_trees[second_tree][1]
        else:
            enemy_element_2 = second_tree
    
    base = 15
    c = class_mods[enemy_class]
    e = element_mods[enemy_element]
    enemy_stats = {
        'HP':  base + e['HP'] + enemy_level,
        'ATK': base + c['ATK'] + e['ATK'] + enemy_level,
        'DEF': base + c['DEF'] + e['DEF'] + enemy_level,
        'ETK': base + c['ETK'] + e['ETK'] + enemy_level,
        'EDF': base + c['EDF'] + e['EDF'] + enemy_level,
        'EVN': base + c['EVN'] + e['EVN'] + enemy_level,
        'SPD': base + c['SPD'] + e['SPD'] + enemy_level,
        'AFT': base + c['AFT'] + e['AFT'] + enemy_level,
    }
    enemy = {
        'name': 'Dim ' + enemy_element + ' ' + enemy_class,
        'element': enemy_element,
        'element_2': enemy_element_2,
        'class': enemy_class,
        'level': enemy_level,
        'stats': enemy_stats,
        'max_hp': enemy_stats['HP']
    }
    return enemy

def battle(name, stats, region, difficulty, player_level):
    enemy = create_enemy(region, difficulty, player_level)
    player_hp = stats['HP']
    enemy_hp = enemy['stats']['HP']
    level = int(player_level)
    max_ep = int((stats['ETK'] + stats['EDF']) * 0.75)
    player_ep = max_ep
    enemy_max_ep = int((enemy['stats']['ETK'] + enemy['stats']['EDF']) *0.75)
    enemy_ep = enemy_max_ep

    print('')
    print(YELLOW + BOLD + '--- BATTLE ---' + RESET)
    print('A ' + enemy['name'] + ' (Lv ' + str(enemy['level']) + ') appears!')
    print('')

    while True:
        print('Your HP: ' + str(player_hp) + '/' + str(stats['HP']) + ' EP: ' + str(player_ep) + '/' + str(max_ep))
        print('Enemy HP: ' + str(enemy_hp) + '/' + str(enemy['max_hp']))
        print('')
        print(CYAN + ' 1. Attack (physical)' + RESET)
        if level >= 5 and player_ep >=10:
            print(CYAN + ' 2. EP Attack A' + RESET + ' - 10 EP')
        else:
            print(' 2. EP Attack A - locked')
        print(CYAN + ' 3. Defend' + RESET)
        print(CYAN + ' 4. Use Item' + RESET)
        print(CYAN + ' 5. Flee' + RESET)
        print('')
        action = input('Choose action: ')

        if action == '1':
            damage = max(1, int(((2 * level / 5 + 2) * move_power['basic'] * stats['ATK'] / enemy['stats']['DEF']) / 70 + 2))
            enemy_hp = enemy_hp - damage
            print('You strike for ' + str(damage) + ' damage!')
        elif action == '2':
            if level < 5 or player_ep < 10:
                print('Cannot use that attack.')
                continue
            damage = max(1, int(((2 * level / 5 + 2) * move_power['A'] * stats['ETK'] / enemy['stats']['EDF']) / 70 + 2))
            enemy_hp = enemy_hp - damage
            player_ep = player_ep - 10
            print('You unleash elemental force for ' + str(damage) + ' damage!')
        elif action == '3':
            print('You brace yourself.')
        elif action == '4':
            print('[Item placeholder]')
            continue
        elif action == '5':
            print('You flee from the battle!')
            return 'fled'
        else:
            print('Invalid choice.')
            continue

        if enemy_hp <= 0:
            print('')
            print('The ' + enemy['name'] + ' fades into darkness.')
            print('Victory!')
            return True
        
        print('')
        enemy_damage = max(1, int(((2 * enemy['level'] / 5 + 2) * move_power['basic'] * enemy['stats']['ATK'] / stats['DEF']) / 70 + 2))
        if action == '3':
            enemy_damage = max(1, int(enemy_damage * 0.5))
        player_hp = player_hp - enemy_damage
        print('The ' + enemy['name'] + ' strikes for ' + str(enemy_damage) + ' damage!')

        if player_hp <= 0:
            print('')
            print('You have fallen...')
            return False
        
        player_ep = min(max_ep, player_ep + int(max_ep * 0.05))
        enemy_ep = min(enemy_max_ep, enemy_ep + int(enemy_max_ep * 0.05))
        print('')
                                                          
# Title screen
while True:
    print(YELLOW + BOLD + '================================' + RESET)
    print(WHITE  + BOLD + '         OF NOBLE LIGHT         ' + RESET)
    print(YELLOW + BOLD + '================================' + RESET)
    print('')
    print('            MAIN MENU           ')
    print('')
    print(CYAN + ' 1. New Game' + RESET)
    print(CYAN + ' 2. Continue' + RESET)
    print(CYAN + ' 3. Delete Game' + RESET)
    print(CYAN + ' 4. Quit' + RESET)
    print('')

    choice = input('Pick an option: ')

    if choice == '1':
        if os.path.exists('txt_rpg/save.txt'):
            print('')
            print('A save file already exists. Starting a new game will overwrite it.')
            confirm = input('Continue? (y/n): ')
            if confirm != 'y':
                continue
        print('')
        print(YELLOW + BOLD + '--- NEW GAME ---' + RESET)
        print('')
        name = input('Enter your name: ')
        print('')
        print('Welcome, ' + name + '.')
        while True:
            print('')
            print(YELLOW + BOLD + '--- CHOOSE YOUR CLASS ---' + RESET)
            print('')
            print(CYAN + ' 1. Warrior' + RESET + ' - physical fighter, close range, weapon specialist')
            print(CYAN + ' 2. Caster' + RESET + ' - physical fighter, long range, positioning expert')
            print(CYAN + ' 3. Sage' + RESET + ' - elemental fighter, close range, elemental combat and healing')
            print(CYAN + ' 4. Magi' + RESET + ' - elemental fighter, long range, elemental offense and healing')
            print('')
            class_choice = input('Pick a class: ')
            if class_choice == '1':
                player_class = 'Warrior'
                break
            elif class_choice == '2':
                player_class = 'Caster'
                break
            elif class_choice == '3':
                player_class = 'Sage'
                break
            elif class_choice == '4':
                player_class = 'Magi'
                break
            else:
                print('Invalid choice.')
        while True:
            print('')
            print(YELLOW + BOLD + '--- CHOOSE YOUR ELEMENT ---' + RESET)
            print('')
            print(' 1. ' + EARTH + ' EARTH ' + RESET + ' - slow, heavy defense, high HP')
            print(' 2. ' + AIR + ' AIR ' + RESET + ' - fast, evasive, high speed')
            print(' 3. ' + FIRE + ' FIRE ' + RESET + ' - aggressive, high attack')
            print(' 4. ' + WATER + ' WATER ' + RESET + ' - balanced, adaptive')
            print('')
            element_choice = input('Pick an element: ')
            if element_choice == '1':
                player_element = 'Earth'
                break
            elif element_choice == '2':
                player_element = 'Air'
                break
            elif element_choice == '3':
                player_element = 'Fire'
                break
            elif element_choice == '4':
                player_element = 'Water'
                break
            else:
                print('Invalid choice.')
        print('')
        print('You are ' + name + ', ' + player_class + ' of ' + player_element + '.')
        with open('txt_rpg/save.txt', 'w') as file:
            file.write(name + '\n')
            file.write(player_class + '\n')
            file.write(player_element + '\n')
            file.write('None\n')
            file.write('0\n')
            file.write('0\n')
        print('Game saved.')
        stats = create_stats(player_class, player_element)
        show_stats(name, player_class, player_element, 'None', '0', stats, 0)
        game_hub(name, player_class, player_element, 'None', '0', stats, 0)                             
    elif choice == '2':
        if not os.path.exists('txt_rpg/save.txt'):
            print('No save file found.')
        else:
            with open('txt_rpg/save.txt', 'r') as file:
                lines = file.readlines()
            name = lines[0].strip()
            player_class = lines[1].strip()
            player_element = lines[2].strip()
            player_element_2 = lines[3].strip()
            player_level = lines[4].strip()
            player_xp = int(lines[5].strip())
            print('')
            print('Welcome back, ' + name + '.')
            print('Level ' + player_level + ' ' + player_class + ' of ' + player_element + '.')
            if player_element_2 != 'None':
                print('Second element: ' + player_element_2)
            stats = create_stats(player_class, player_element)
            show_stats(name, player_class, player_element, player_element_2, player_level, stats, player_xp)
            game_hub(name, player_class, player_element, player_element_2, player_level, stats, player_xp)                             
    elif choice == '4':
        break
    elif choice == '3':
        if not os.path.exists('txt_rpg/save.txt'):
            print('No save file found.')
        else:
            print('')
            print('Are you sure? This cannot be undone.')
            confirm = input('Delete save? (y/n): ')
            if confirm == 'y':
                os.remove('txt_rpg/save.txt')
                print('Save file deleted.')
            else:
                print('Cancelled.')
    else:
        print('Invalid choice')