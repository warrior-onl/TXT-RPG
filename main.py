# OF NOBLE LIGHT - txt_rpg

import os

# Text colors
RESET  = '\033[0'
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
        'AFT': base + c['AFT'] + e['SPD'],
    }
    return stats

def show_stats(name, player_class, element_1, element_2, level, stats):
    print('')
    print(YELLOW + BOLD + '--- CHARACTER ---' + RESET)
    print('Name:   ' + name)
    print('Class:  ' + player_class)
    print('Element:' + element_1)
    if element_2 != 'None':
        print('Slot 2: ' + element_2)
    print('Level:  ' + level)
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
