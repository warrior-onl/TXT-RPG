# OF NOBLE LIGHT - txt_rpg

import os

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
STORM = '\033[1m\033[42m\033[97m'
MAGMA = '\033[1m\033[41m\033[97m'
ICE   = '\033[1m\033[106m\033[97m'
# Evolved element colors
NATURE   = '\033[1m\033[40m\033[97m'
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

def show_stats(name, player_class, element_1, element_2, level, stats):
    print('')
    print(YELLOW + BOLD + '--- CHARACTER ---' + RESET)
    print('Name:    ' + name)
    print('Class:   ' + player_class)
    print('Element: ' + element_1)
    if element_2 != 'None':
        print('Slot 2: ' + element_2)
    print('Level:   ' + level)
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

def game_hub(name, player_class, player_element, player_element_2, player_level, stats):
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
            print('Entering ' + region + ' Region...')
        elif hub_choice == '2':
            show_stats(name, player_class, player_element, player_element_2, player_level, stats)
        elif hub_choice == '3':
            with open('txt_rpg/save.txt', 'w') as file:
                file.write(name + '\n')
                file.write(player_class + '\n')
                file.write(player_element + '\n')
                file.write(player_element_2 + '\n')
                file.write(player_level + '\n')
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
        else:
            print('Invalid choice.')

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
        print('Game saved.')
        stats = create_stats(player_class, player_element)
        show_stats(name, player_class, player_element, 'None', '0', stats)
        game_hub(name, player_class, player_element, 'None', '0', stats)                             
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
            print('')
            print('Welcome back, ' + name + '.')
            print('Level ' + player_level + ' ' + player_class + ' of ' + player_element + '.')
            if player_element_2 != 'None':
                print('Second element: ' + player_element_2)
            stats = create_stats(player_class, player_element)
            show_stats(name, player_class, player_element, player_element_2, player_level, stats)
            game_hub(name, player_class, player_element, player_element_2, player_level, stats)                             
    elif choice == '4':
        break
    elif choice == '3':
        print('Delete Game')
    else:
        print('Invalid choice')