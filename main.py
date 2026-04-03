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
# Element name color mapping
element_colors = {
    'Earth'   : EARTH,
    'Air'     : AIR,
    'Water'   : WATER,
    'Fire'    : FIRE,
    'Stone'   : STONE,
    'Storm'   : STORM,
    'Magma'   : MAGMA,
    'Ice'     : ICE,
    'Nature'  : NATURE,
    'Electric': ELECTRIC,
    'Plasma'  : PLASMA,
    'Aether'  : AETHER,
}

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
# Class focus
focus_class = {
    'Warrior': 'Warrior', 'Warden': 'Warrior', 'Arbiter': 'Warrior',
    'Caster': 'Caster', 'Ranger': 'Caster', 'Channeler': 'Caster',
    'Sage': 'Sage', 'Shaman': 'Sage', 'Primal': 'Sage',
    'Magi': 'Magi', 'Alchemist': 'Magi', 'Druid': 'Magi',
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

# Element matchups - attacker vs defender
# 1.30 = advantage, 0.80 = disadvantage, 1.0 = neutral
element_matchups = {
    'Earth': {'Water': 1.30, 'Air': 0.80},
    'Air':   {'Earth': 1.30, 'Fire': 0.80},
    'Fire':  {'Air': 1.30, 'Water': 0.80},
    'Water': {'Fire': 1.30, 'Earth': 0.80},
}

def get_matchup(attacker_element, defender_element, defender_element_2):
    matchups = element_matchups.get(attacker_element, {})
    mult1 = matchups.get(defender_element, 1.0)
    if defender_element_2 != 'None':
        mult2 = matchups.get(defender_element_2, 1.0)
        if mult1 > 1.0 and mult2 < 1.0:
            return 1.0
        elif mult1 < 1.0 and mult2 > 1.0:
            return 1.0
        elif mult1 != 1.0:
            return mult1
        else:
            return mult2
    return mult1

def get_available_attacks(player_element, player_level):
    level = int(player_level)
    attacks = element_attacks.get(player_element, {})
    available = []
    if level >= 5 and 'A' in attacks:
        available.append(attacks['A'])
    if level >= 15 and 'B' in attacks:
        available.append(attacks['B'])
    if level >= 25 and 'C' in attacks:
        available.append(attacks['C'])
    if level >= 35 and 'D' in attacks:
        available.append(attacks['D'])
    if level >= 45 and 'E' in attacks:
        available.append(attacks['E'])
    return available

# Move power Values
move_power = {
    'basic': 60,
    'basic_el': 50,
    'A': 80,
    'B': 100,
    'C': 120,
    'D': 145,
    'E': 170,
}

# Element attack data: name, stat type, EP cost, power tier
element_attacks = {
    'Earth': {
        'A': {'name': 'Mud Slide', 'stat': 'ATK', 'cost': 10, 'power': 'A'},
        'B': {'name': 'Clay Skin', 'stat': 'buff', 'cost': 25, 'power': 'B'},
        'C': {'name': 'Tremor', 'stat': 'ATK', 'cost': 45, 'power': 'C'},
        'D': {'name': 'Sandstorm', 'stat': 'ETK', 'cost': 70, 'power': 'D'},
        'E': {'name': 'Earthquake', 'stat': 'ATK', 'cost': 100, 'power': 'E'},
    },
    'Air': {
        'A': {'name': 'Gust', 'stat': 'ETK', 'cost': 10, 'power': 'A'},
        'B': {'name': 'Air Blade', 'stat': 'ATK', 'cost': 25, 'power': 'B'},
        'C': {'name': 'Tailwind', 'stat': 'buff', 'cost': 45, 'power': 'C'},
        'D': {'name': 'Cyclone', 'stat': 'ETK', 'cost': 70, 'power': 'D'},
        'E': {'name': 'Hurricane', 'stat': 'ETK', 'cost': 100, 'power': 'E'},
    },
    'Fire': {
        'A': {'name': 'Flare', 'stat': 'ETK', 'cost': 10, 'power': 'A'},
        'B': {'name': 'Fire Dance', 'stat': 'ATK', 'cost': 25, 'power': 'B'},
        'C': {'name': 'Overheat', 'stat': 'buff', 'cost': 45, 'power': 'C'},
        'D': {'name': 'Scorched Earth', 'stat': 'ETK', 'cost': 70, 'power': 'D'},
        'E': {'name': 'Hellfire', 'stat': 'ATK', 'cost': 100, 'power': 'E'},
    },
    'Water': {
        'A': {'name': 'Soak', 'stat': 'ETK', 'cost': 10, 'power': 'A'},
        'B': {'name': 'Riptide', 'stat': 'ATK', 'cost': 25, 'power': 'B'},
        'C': {'name': 'Flood', 'stat': 'ETK', 'cost': 45, 'power': 'C'},
        'D': {'name': 'Tidal Surge', 'stat': 'ATK', 'cost': 70, 'power': 'D'},
        'E': {'name': 'Tsunami', 'stat': 'ETK', 'cost': 100, 'power': 'E'},
    },
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

def check_level_up(player_level, player_xp, player_class, player_element, player_element_2, stats):
    level = int(player_level)
    while level < 100:
        xp_needed = level * 25 + 10
        if player_xp < xp_needed:
            break
        player_xp = player_xp - xp_needed
        level = level + 1
        mult = 0.151 + (0.001 * level)
        c = class_mods[player_class]
        e = element_mods[player_element]
        hp_boost = 12 + e['HP']
        if player_element_2 != 'None':
            e2 = element_mods[player_element_2]
            hp_boost = hp_boost + e2['HP']
        stats['HP'] = stats['HP'] + max(1, int(hp_boost * mult))
        for stat in ['ATK', 'DEF', 'ETK', 'EDF', 'EVN', 'SPD', 'AFT']:
            boost = 8 + c[stat] + e[stat]
            if player_element_2 != 'None':
                boost = boost + e2[stat]
            stats[stat] = stats[stat] + max(1, int(boost * mult))
        print('')
        print(YELLOW + BOLD + '*** LEVEL UP! Level ' + str(level) + ' ***' + RESET)
    return str(level), player_xp, stats

def show_stats(name, player_class, element_1, element_2, level, stats, player_xp):
    print('')
    print(YELLOW + BOLD + '--- CHARACTER ---' + RESET)
    print('Name:    ' + name)
    print('Class:   ' + player_class)
    print('Element: ' + element_colors.get(element_1, '') + ' ' + element_1 + ' ' + RESET)
    if element_2 != 'None':
        print('Slot 2:  ' + element_colors.get(element_2, '') + ' ' + element_2 + ' ' + RESET)
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
                result = run_path(path, region, difficulty, name, player_class, player_element, player_element_2, stats, player_level, player_xp)
                if result in ['lost', 'fled']:
                    run_ended = True
                    break
                else:
                    player_xp, player_level = result
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
                file.write(str(stats['HP']) + '\n')
                file.write(str(stats['ATK']) + '\n')
                file.write(str(stats['DEF']) + '\n')
                file.write(str(stats['ETK']) + '\n')
                file.write(str(stats['EDF']) + '\n')
                file.write(str(stats['EVN']) + '\n')
                file.write(str(stats['SPD']) + '\n')
                file.write(str(stats['AFT']) + '\n')
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

def run_path(path_number, region, difficulty, name, player_class, player_element, player_element_2, stats, player_level, player_xp):
    print('')
    print(YELLOW + BOLD + '--- Path ' + str(path_number) + ' of 4 ---' + RESET)
    print('')
    print('You come to a fork in the road.')
    print('')
    while True:
        print(CYAN + ' 1. Left' + RESET)
        print(CYAN + ' 2. Right' + RESET)
        print(CYAN + ' 3. View Character' + RESET)
        print(CYAN + ' 4. Return to Base' + RESET)
        print('')
        fork = input('Which way? ')
        if fork in ['1', '2']:
            break
        elif fork == '3':
            show_stats(name, player_class, player_element, player_element_2, player_level, stats, player_xp)
        elif fork == '4':
            return 'fled'
        else:
            print('Invalid choice.')

    guaranteed = random.randint(1, 3)
    had_random_battle = False

    for stop in range(1, 4):
        print('')
        print(WHITE + '--- Stop ' + str(stop) + ' of 3 ---' + RESET)

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
            result = battle(name, stats, region, difficulty, player_level, player_element, player_element_2)
            if result == False:
                print('Your journey ends here...')
                return 'lost'
            elif result == 'fled':
                print('You retreat back to base.')
                return 'fled'
            else:
                level = int(player_level)
                ratio = max(0.1, 1 - (level * 0.008))
                xp_gained = max(1, int(result * 10 * ratio))
                player_xp = player_xp + xp_gained
                print('Gained ' + str(xp_gained) + ' XP!')
                player_level, player_xp, stats = check_level_up(player_level, player_xp, player_class, player_element, player_element_2, stats)
            had_random_battle = True
        elif encounter == 'nothing':
            print('The path is quiet. You press forward.')
        elif encounter == 'traveler':
            print('You spot a traveler on the road ahead.')
            print('[Traveler placeholder]')
        elif encounter == 'loot':
            print('You spot something glinting off the path.')
            print('[Loot placeholder]')
    return player_xp, player_level

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

def player_attack(action, level, stats, enemy, enemy_hp, move_power, player_element, selected_attack):
    matchup = get_matchup(player_element, enemy['element'], enemy['element_2'])
    if action == '1':
        damage = max(1, int(((2 * level / 5 + 2) * move_power['basic'] * stats['ATK'] / enemy['stats']['DEF']) / 70 + 2))
        damage = int(damage * matchup)
        crit = random.randint(1, 100) <= 5
        if crit:
            damage = int(damage * 1.5)
        enemy_hp = enemy_hp - damage
        if crit:
            print(YELLOW + 'CRITICAL HIT! ' + RESET + 'You strike for ' + str(damage) + ' damage!')
        else:
            print('You strike for ' + str(damage) + ' damage!')
    elif action == '2':
        damage = max(1, int(((2 * level / 5 + 2) * move_power['basic_el'] * stats['ETK'] / enemy['stats']['EDF']) / 70 + 2))
        damage = int(damage * matchup)
        crit = random.randint(1, 100) <= 5
        if crit:
            damage = int(damage * 1.5)
        enemy_hp = enemy_hp - damage
        status_roll = random.randint(1, 100)
        if crit and status_roll <= 5:
            print(YELLOW + 'CRITICAL HIT! ' + RESET + 'You unleash elemental force for ' + str(damage) + ' damage! Status effect applied!')
        elif crit:
            print(YELLOW + 'CRITICAL HIT! ' + RESET + 'You unleash elemental force for ' + str(damage) + ' damage!')
        elif status_roll <= 5:
            print('You unleash elemental force for ' + str(damage) + ' damage! Status effect applied!')
        else:
            print('You unleash elemental force for ' + str(damage) + ' damage!')
    elif selected_attack is not None:
        el_color = element_colors.get(player_element, '')
        power = move_power[selected_attack['power']]
        if selected_attack['stat'] == 'ATK':
            damage = max(1, int(((2 * level / 5 + 2) * power * stats['ATK'] / enemy['stats']['DEF']) / 70 + 2))
        elif selected_attack['stat'] == 'ETK':
            damage = max(1, int(((2 * level / 5 + 2) * power * stats['ETK'] / enemy['stats']['EDF']) / 70 + 2))
        elif selected_attack['stat'] == 'buff':
            print(el_color + ' ' + selected_attack['name'] + ' ' + RESET + ' [Buff placeholder]')
            return enemy_hp
        damage = int(damage * matchup)
        crit = random.randint(1, 100) <= 5
        if crit:
            damage = int(damage * 1.5)
        enemy_hp = enemy_hp - damage
        if crit:
            print(YELLOW + 'CRITICAL HIT! ' + RESET + el_color + ' ' + selected_attack['name'] + ' ' + RESET + ' deals ' + str(damage) + ' damage!')
        else:
            print(el_color + ' ' + selected_attack['name'] + ' ' + RESET + ' deals ' + str(damage) + ' damage!')
    return enemy_hp

def enemy_turn(enemy, enemy_hp, player_hp, stats, move_power, player_element, player_element_2, enemy_ep, enemy_max_ep):
    matchup = get_matchup(enemy['element'], player_element, player_element_2)
    enemy_color = element_colors.get(enemy['element'], '')
    enemy_display = 'Dim ' + enemy_color + ' ' + enemy['element'] + ' ' + RESET + enemy['class']
    hp_percent = enemy_hp / enemy['max_hp']

    if hp_percent <= 0.20:
        print('The ' + enemy_display + ' braces itself.')
        return player_hp, enemy_ep, True
    
    use_etk = enemy['stats']['ETK'] > enemy['stats']['ATK']

    if enemy['level'] >= 5 and enemy_ep >= 10:
        if use_etk:
            enemy_damage = max(1, int(((2* enemy['level'] / 5 + 2) * move_power['A'] * enemy['stats']['ETK'] / stats['EDF']) / 70 + 2))
        else:
            enemy_damage = max(1, int(((2* enemy['level'] / 5 + 2) * move_power['A'] * enemy['stats']['ATK'] / stats['DEF']) / 70 + 2))
        enemy_ep = enemy_ep - 10
        enemy_damage = int(enemy_damage * matchup)
        crit = random.randint(1, 100) <= 5
        if crit:
            enemy_damage = int(enemy_damage * 1.5)
        player_hp = player_hp - enemy_damage
        if use_etk:
            if crit:
                print(YELLOW + 'CRITICAL HIT! ' + RESET + 'The ' + enemy_display + ' channels elemental power for ' + str(enemy_damage) + ' damage!')
            else:
                print('The ' + enemy_display + ' channels elemental power for ' + str(enemy_damage) + ' damage!')
        else:
            if crit:
                print(YELLOW + 'CRITICAL HIT! ' + RESET + 'The ' + enemy_display + ' unleashes a powerful strike for ' + str(enemy_damage) + ' damage!')
            else:
                print('The ' + enemy_display + ' unleashes a powerful strike for ' + str(enemy_damage) + ' damage!')
    else:
        if use_etk:
            enemy_damage = max(1, int(((2 * enemy['level'] / 5 + 2) * move_power['basic_el'] * enemy['stats']['ETK'] / stats['EDF']) / 70 + 2))
        else:
            enemy_damage = max(1, int(((2 * enemy['level'] / 5 + 2) * move_power['basic'] * enemy['stats']['ATK'] / stats['DEF']) / 70 + 2))
        enemy_damage = int(enemy_damage * matchup)
        crit = random.randint(1, 100) <= 5
        if crit:
            enemy_damage = int(enemy_damage * 1.5)
        player_hp = player_hp - enemy_damage
        if use_etk:
            if crit:
                print(YELLOW + 'CRITICAL HIT! ' + RESET + 'The ' + enemy_display +' strikes with elemental force for ' + str(enemy_damage) + ' damage!')
            else:
                print('The ' + enemy_display + ' strikes with elemental force for ' + str(enemy_damage) + ' damage!')
        else:
            if crit:
                print(YELLOW + 'CRITICAL HIT! ' + RESET + 'The ' + enemy_display + ' strikes for ' + str(enemy_damage) + ' damage!')
            else:
                print('The ' + enemy_display + ' strikes for ' + str(enemy_damage) + ' damage!')

    return player_hp, enemy_ep, False        

def battle(name, stats, region, difficulty, player_level, player_element, player_element_2):
    enemy = create_enemy(region, difficulty, player_level)
    player_hp = stats['HP']
    enemy_hp = enemy['stats']['HP']
    level = int(player_level)
    max_ep = int((stats['ETK'] + stats['EDF']) * 0.75)
    player_ep = max_ep
    enemy_max_ep = int((enemy['stats']['ETK'] + enemy['stats']['EDF']) *0.75)
    enemy_ep = enemy_max_ep
    enemy_color = element_colors.get(enemy['element'], '')
    enemy_display = 'Dim ' + enemy_color + ' ' + enemy['element'] + ' ' + RESET + enemy['class']

    print('')
    print(YELLOW + BOLD + '--- BATTLE ---' + RESET)
    print('A ' + enemy_display + ' (Lv ' + str(enemy['level']) + ') appears!')
    print('')

    available_attacks = get_available_attacks(player_element, player_level)
    el_color = element_colors.get(player_element, '')
    focus_buffs = {}
    saved_stats = {}
    
    while True:
        print('Your HP: ' + str(player_hp) + '/' + str(stats['HP']) + ' EP: ' + str(player_ep) + '/' + str(max_ep))
        print('Enemy HP: ' + str(enemy_hp) + '/' + str(enemy['max_hp']))
        print('')
        print(CYAN + ' 1. Attack' + RESET)
        print(CYAN + ' 2. Defend' + RESET)
        print(CYAN + ' 3. Bag' + RESET)
        print(CYAN + ' 4. Flee' + RESET)
        print('')
        main_choice = input('Choose action: ')

        if main_choice not in ['1', '2', '3', '4']:
            print('Invalid choice.')
            continue
        if main_choice == '4':
            print('You flee from the battle!')
            return 'fled'
        if main_choice == '3':
            print('[Bag placeholder]')
            continue

        action = None
        selected_attack = None
        player_defending = False

        if main_choice == '1':
            print('')
            print(CYAN + ' 1. Physical Attack' + RESET)
            print(CYAN + ' 2. Elemental Attack' + RESET)
            for i, atk in enumerate(available_attacks):
                num = 3 + i
                if atk['stat'] == 'buff':
                    label = atk['name'] + ' (buff) - ' + str(atk['cost']) + ' EP'
                else:
                    label = atk['name'] + ' - ' + str(atk['cost']) + ' EP'
                if player_ep >= atk['cost']:
                    print(el_color + ' ' + str(num) + '. ' + label + ' ' + RESET)
                else:
                    print(' ' + str(num) + '. ' + label + ' - not enough EP')
            back_num = 3 + len(available_attacks)
            print(CYAN + ' ' + str(back_num) + '. Back' + RESET)
            print('')
            atk_choice = input('Choose attack: ')
            valid_atk = [str(x) for x in range(1, back_num + 1)]
            if atk_choice not in valid_atk:
                print('Invalid choice.')
                continue
            if atk_choice == str(back_num):
                continue
            atk_num = int(atk_choice)
            if atk_choice in ['1', '2']:
                action = atk_choice
            elif atk_num >= 3 and atk_num < back_num:
                attack_index = atk_num - 3
                selected_attack = available_attacks[attack_index]
                if player_ep < selected_attack['cost']:
                    print('Not enough EP.')
                    continue

        elif main_choice == '2':
            print('')
            print(CYAN + ' 1. Basic Defend' + RESET + ' - free')
            def_options = ['basic']
            next_num = 2
            if level >= 10:
                if player_ep >= 25:
                    print(el_color + ' ' + str(next_num) + '. Elemental Defend - 25 EP ' + RESET)
                else:
                    print(' ' + str(next_num) + '. Elemental Defend - not enough EP')
                def_options.append('elemental')
                next_num = next_num + 1
            if level >= 30:
                if player_ep >= 75:
                    print(el_color + ' ' + str(next_num) + '. Great Defend - 75 EP ' + RESET)
                else:
                    print(' ' + str(next_num) + '. Great Defend - not enough EP')
                def_options.append('great')
                next_num = next_num + 1
            print(CYAN + ' ' + str(next_num) + '. Focus' + RESET + ' - free')
            def_options.append('focus')
            next_num = next_num + 1
            print(CYAN + ' ' + str(next_num) + '. Back' + RESET)
            print('')
            def_choice = input('Choose option: ')
            valid_def = [str(x) for x in range(1, next_num + 1)]
            if def_choice not in valid_def:
                print('Invalid choice.')
                continue
            if def_choice == str(next_num):
                continue
            picked = def_options[int(def_choice) - 1]
            if picked == 'elemental' and player_ep < 25:
                print('Not enough EP.')
                continue
            if picked == 'great' and player_ep < 75:
                print('Not enough EP.')
                continue
            if picked in ['basic', 'elemental', 'great']:
                player_defending = picked
            elif picked == 'focus':
                base = focus_class[player_class]
                if base == 'Magi':
                    ep_back = int(max_ep * 0.30)
                else:
                    ep_back = int(max_ep * 0.25)
                player_ep = min(max_ep, player_ep + ep_back)
                print('You focus your energy. Recovered ' + str(ep_back) + ' EP.')
                if base == 'Warrior':
                    focus_buffs = {'ATK': int(stats['ATK'] * 0.10)}
                elif base == 'Caster':
                    focus_buffs = {'ATK': int(stats['ATK'] * 0.10)}
                elif base == 'Sage':
                    focus_buffs = {'DEF': int(stats['DEF'] * 0.05), 'EVN': int(stats['EVN'] * 0.05)}
                elif base == 'Magi':
                    focus_buffs = {'ETK': int(stats['ETK'] * 0.10)}
        if focus_buffs:
            saved_stats = {}
            for stat in focus_buffs:
                saved_stats[stat] = stats[stat]
                stats[stat] = stats[stat] + focus_buffs[stat]
        player_faster = stats['SPD'] >= enemy['stats']['SPD']

        if player_defending:
            if player_defending == 'basic':
                def_mult = 0.50
                evn_mult = 0.25
            elif player_defending == 'elemental':
                def_mult = 0.25
                evn_mult = 0.50
                player_ep = player_ep - 25
            elif player_defending == 'great':
                def_mult = 0.75
                evn_mult = 0.50
                player_ep = player_ep - 75
            def_boost = int(stats['DEF'] * def_mult)
            edf_boost = int(stats['EDF'] * def_mult)
            evn_boost = int(stats['EVN'] * evn_mult)
            stats['DEF'] = stats['DEF'] + def_boost
            stats['EDF'] = stats['EDF'] + edf_boost
            stats['EVN'] = stats['EVN'] + evn_boost
            print('You brace yourself.')
            print('')
            player_hp, enemy_ep, enemy_defending = enemy_turn(enemy, enemy_hp, player_hp, stats, move_power, player_element, player_element_2, enemy_ep, enemy_max_ep)
            stats['DEF'] = stats['DEF'] - def_boost
            stats['EDF'] = stats['EDF'] - edf_boost
            stats['EVN'] = stats['EVN'] - evn_boost
        elif player_defending == False and action is None and selected_attack is None:
            player_hp, enemy_ep, enemy_defending = enemy_turn(enemy, enemy_hp, player_hp, stats, move_power, player_element, player_element_2, enemy_ep, enemy_max_ep)
        elif player_faster:
            enemy_hp = player_attack(action, level, stats, enemy, enemy_hp, move_power, player_element, selected_attack)
            if selected_attack is not None:
                player_ep = player_ep - selected_attack['cost']
            if enemy_hp <= 0:
                print('')
                print('The ' + enemy_display + ' fades into darkness.')
                print('Victory!')
                return enemy['level']
            print('')
            player_hp, enemy_ep, enemy_defending = enemy_turn(enemy, enemy_hp, player_hp, stats, move_power, player_element, player_element_2, enemy_ep, enemy_max_ep)
        else:
            player_hp, enemy_ep, enemy_defending = enemy_turn(enemy, enemy_hp, player_hp, stats, move_power, player_element, player_element_2, enemy_ep, enemy_max_ep)
            if player_hp <= 0:
                print('')
                print('You have fallen...')
                return False
            print('')
            enemy_hp = player_attack(action, level, stats, enemy, enemy_hp, move_power, player_element, selected_attack)
            if selected_attack is not None:
                player_ep = player_ep - selected_attack['cost']

        if enemy_hp <= 0:
            print('')
            print('The ' + enemy_display + ' fades into darkness.')
            print('Victory!')
            return enemy['level']

        if player_hp <= 0:
            print('')
            print('You have fallen...')
            return False

        player_ep = min(max_ep, player_ep + int(max_ep * 0.05))
        enemy_ep = min(enemy_max_ep, enemy_ep + int(enemy_max_ep * 0.05))
        if saved_stats:
            for stat in saved_stats:
                stats[stat] = saved_stats[stat]
            saved_stats = {}
            focus_buffs = {}
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
        stats = create_stats(player_class, player_element)
        with open('txt_rpg/save.txt', 'w') as file:
            file.write(name + '\n')
            file.write(player_class + '\n')
            file.write(player_element + '\n')
            file.write('None\n')
            file.write('0\n')
            file.write('0\n')
            file.write(str(stats['HP']) + '\n')
            file.write(str(stats['ATK']) + '\n')
            file.write(str(stats['DEF']) + '\n')
            file.write(str(stats['ETK']) + '\n')
            file.write(str(stats['EDF']) + '\n')
            file.write(str(stats['EVN']) + '\n')
            file.write(str(stats['SPD']) + '\n')
            file.write(str(stats['AFT']) + '\n')
        print('Game saved.')
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
            stats = {
                'HP': int(lines[6].strip()),
                'ATK': int(lines[7].strip()),
                'DEF': int(lines[8].strip()),
                'ETK': int(lines[9].strip()),
                'EDF': int(lines[10].strip()),
                'EVN': int(lines[11].strip()),
                'SPD': int(lines[12].strip()),
                'AFT': int(lines[13].strip()),
            }
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