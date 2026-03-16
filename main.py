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

# Class stat modifiers
class_mods = {
    'Warrior': {'ATK': 2, 'DEF': 2, 'ETK': 0, 'EDF': 0, 'EVN': 1, 'SPD': 0, 'AFT': 0},
    'Caster':  {'ATK': 2, 'DEF': 1, 'ETK': 1, 'EDF': 0, 'EVN': 0, 'SPD': 1, 'AFT': 0},
    'Sage':    {'ATK': 0, 'DEF': 0, 'ETK': 1, 'EDF': 1, 'EVN': 1, 'SPD': 1, 'AFT': 1},
    'Magi':    {'ATK': 0, 'DEF': 0, 'ETK': 2, 'EDF': 2, 'EVN': 0, 'SPD': 0, 'AFT': 1},
}

# Element stat modifiers
element_mods = {
    'Earth':  {'HP': 5, 'ATK': 1, 'DEF': 3, 'ETK': 1, 'EDF': 2, 'EVN': -1, 'SPD': -1, 'AFT': 0},
    'Air':    {'HP': 2, 'ATK': -1, 'DEF': -1, 'ETK': 2, 'EDF': 1, 'EVN': 3, 'SPD': 4, 'AFT': 0},
    'Fire':   {'HP': -2, 'ATK': 4, 'DEF': 0, 'ETK': 4, 'EDF': 0, 'EVN': 2, 'SPD': 2, 'AFT': 0},
    'Water':  {'HP': 6, 'ATK': 0, 'DEF': 1, 'ETK': 0, 'EDF': 1, 'EVN': 1, 'SPD': 0, 'AFT': 1},
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
            print('Region select coming soon.')
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