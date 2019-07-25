# Програма полностью работает без {yellow}, {color_end}
# Если вместо цвета у вас выводится набор символов, поменяйть строки 7 и 8 на
# yellow = '' и color_end = ''

# Системное (Работает только в PyCharm)

yellow = '\x1b[1;93m'
color_end = '\x1b[0m'

# Функции


def stats(person):
    statistics = \
        f'|{"Имя":^{len(hero["name"]) + 4}}|' \
        f'{"Броня":^7}|' \
        f'{"Урон":^6}|' \
        f'{"Здоровье":^10}|\n' \
        f'|{yellow}{person["name"]:^{len(hero["name"]) + 4}}{color_end}|' \
        f'{yellow}{person["armor"]:^7}{color_end}|' \
        f'{yellow}{person["damage"]:^6}{color_end}|' \
        f'{yellow}{person["hp"]:^10}{color_end}|'
    print(statistics)
    print()


def do_help():
    menu = \
        '|' + '- ' * 25 + '|\n' \
        f'|{"Меню":^50}|\n' \
                          '|' + '- ' * 25 + '|\n'
    for i in range(len(commands)):
        menu_string = f'{commands[i]} - {commands_desc[i]}'
        menu += \
            f'|{menu_string:^50}|\n' \
            '|' + '- ' * 25 + '|\n'
    print(menu)


def start(h, es):
    print(
        'Привет это снова я - Дэкой. '
        'Ну что готов к своему первому заданию? Видишь этот склеп на вершине холма?\n'
        'В него уже на заходили 23 года. '
        'Говорят там завелось много чудовищь.\n'
        f'Это задание должно быть легким для тебя, еще и мешок золота от {yellow}Гревиаса{color_end} получишь!\n'
        f'{h [ "name" ]} заходит в склеп и видит несколько комнат. '
        'Из каждой доносятся устрашающие звуки.\n'
        'Вы решили осматривать каждую комнату по порядку.'
    )
    fight_break = fight_all(h, es)

    return (hero['hp'] > 0) and not (fight_break)


def fight_all(h, es):
    i = 1
    fight_break = False
    for e in es:
        print(f'Вы заходите в {yellow}{i}{color_end} комнату и видите в темном углу страшное существо:\n')
        stats(e)
        fight_break = fight(h, e)
        if fight_break:
            break
        i += 1

        if h['hp'] <= 0:
            print(f'Враг оказался сильнее, {yellow}{h["name"]}{color_end}.')
            break

        if e['hp'] <= 0:
            print(
                f'Отличный бой, {yellow}{h["name"]}{color_end}. '
                f'Ты победил!\n')
        do_chest(h, chest)

    return fight_break


def fight(h, e):
    is_break = False
    while e['hp'] > 0 and h['hp'] > 0:
        agree = input(
            f'Выберите вариант хода?\n'
            f' 1 - Стандарт,\n'
            f' 2 - Атака ({move_rules["attack"]["damage_kf"]}x урон и {move_rules["attack"]["armor_kf"]}x броня),\n'
            f' 3 - Защита ({move_rules["defence"]["damage_kf"]}x урон и {move_rules["defence"]["armor_kf"]}x броня),\n'
            f' Другая клавиша - прервать бой \n')

        if agree == '1':
            x = 'default'
        elif agree == '2':
            x = 'attack'
        elif agree == '3':
            x = 'defence'
        else:
            print('Вы прервали бой.')
            is_break = True
            break
        fight_round(h, e, x)
        if e['hp'] <= 0:
            break

    return is_break


def fight_round(h, e, x):
    if h['damage'] * move_rules[x]["damage_kf"] >= e['armor']:
        e['hp'] -= hero['damage'] * move_rules[x]["damage_kf"] - e['armor']
        if e['hp'] <= 0:
            return
    if e['damage'] * move_rules[x]["damage_kf"] >= hero['armor']:
        hero['hp'] -= e['damage'] - hero['armor'] * move_rules[x]["armor_kf"]

    if e['hp'] > 0:
        print(f'Великолепный удар: Здоровье врага - {yellow}{e["hp"]}{color_end}, '
              f'Ваше здоровье - {yellow}{hero["hp"]}{color_end}')


def do_chest(h, ch):
    print(
        'Вам открылся сундук "Великих". '
        'Выберите награду.')

    s = ''
    for j in range(len(ch)):
        print(f'err107{ch}')
        s += f'{j + 1} - {ch[j]}\n'

    if s == '':
        print('Сундук пуст.\n')

    else:
        while True:
            j = input(s + f'{len(ch) + 1} - Оставить всё как есть.')
            if j.isdigit():
                if int(j) - 1 < len(ch) + 1:
                    j = int(j)
                    break
            print(f'Введите значение от 1 до {len(ch) + 1}.')

        if j - 1 < len(ch):
            if ch[j - 1] == 'восстановить здоровье полностью':
                h['hp'] = h['max_hp']
            elif ch[j - 1] == 'увеличить максимальное здоровье':
                h['max_hp'] *= 1.15
            elif ch[j - 1] == 'увеличить урон':
                h['damage'] *= 1.1
            elif ch[j - 1] == 'увеличить броню':
                h['armor'] *= 1.2
            ch.pop(j - 1)


# Види сущностей
hero = {}

roles = {
    'human': {
        'role_name': 'человек',
        'hp': 800,
        'max_hp': 800,
        'armor': 100,
        'damage': 120,
    },
    'mag': {
        'role_name': 'маг',
        'hp': 460,
        'max_hp': 600,
        'armor': 70,
        'damage': 150,
    },
    'ork': {
        'role_name': 'орк',
        'hp': 900,
        'max_hp': 900,
        'armor': 105,
        'damage': 110,
    },
    'elf': {
        'role_name': 'эльф',
        'hp': 700,
        'max_hp': 700,
        'armor': 80,
        'damage': 130,
    },
}

enemies = [
    {
        'name': 'Сrimson Bloodhunter',
        'hp': 300,
        'armor': 20,
        'damage': 80,
    },
    {
        'name': 'Heaven Vampire',
        'hp': 300,
        'armor': 40,
        'damage': 90,
    },
    {
        'name': 'Magical Wolf',
        'hp': 300,
        'armor': 60,
        'damage': 100,
     },
    {
        'name': 'Ferocious Tiger',
        'hp': 300,
        'armor': 80,
        'damage': 110,
     },
    {
        'name': 'Risen Guard',
        'hp': 300,
        'armor': 100,
        'damage': 120},
]

move_rules = {
    'default': {
        'damage_kf': 1,
        'armor_kf': 1},
    'attack': {
        'damage_kf': 1.3,
        'armor_kf': 0.75},
    'defence': {
        'damage_kf': 0.75,
        'armor_kf': 1.3},
}

chest = [
    'восстановить здоровье полностью',
    'увеличить максимальное здоровье',
    'увеличить урон',
    'увеличить броню',
]

commands = (
    'Start',
    'Stats',
    'Help',
    'Exit'
)

commands_desc = (
    'Начать задание',
    'Статистика',
    'Помощь',
    'Выход'
)

instructor = {
    'hp': 1000,
    'armor': 100,
}

# Ввод базовых переменных
while True:
    hero['name'] = input("Введите имя вашего персонажа: \n").capitalize()
    if hero['name'].strip() != '':
        break
print()
artifact = False

while True:
    hero_class = input('Выберите роль вашего персонажа: Человек, Маг, Орк, Эльф: \n').lower()
    if hero_class == 'человек':
        hero.update(roles['human'])
    elif hero_class == 'маг':
        hero.update(roles['mag'])
    elif hero_class == 'орк':
        hero.update(roles['ork'])
    elif hero_class == 'эльф':
        hero.update(roles['elf'])
    else:
        print('Ошибка. Попробуйте снова')
        continue
    break
print()
train_damage = hero['damage']

# Стандартные фразы
WELCOME = \
    f"Здравствуй, {hero_class} {yellow}{hero['name']}{color_end}!\n" \
    f"Меня зовут {yellow}Дэкой{color_end}. " \
    "Даже не знаю как ты тут оказался, но мы тебе рады. " \
    "Я расскажу тебе о наших краях. "

error_text = \
    'Неизвестная команда. ' \
    f'Ознакомиться с списоком возможных команд можно введя {yellow}Help{color_end}'

LORE = '''
Ты попали в Вальтсардию.
Это маленькое королевство людей с богатой историей.
В нем есть 2 крупных города Верхейм и Рейнварден.
Добро пожаловать!
'''

INTRO = \
    'Я вижу, что ты боец. ' \
    f'Предлагаю тебе устроить спарринг с моим другом {yellow}Фриском{color_end}'

game_exit = 'Увидимся позже! Возвращайся скорее.'

# Вступление
print(WELCOME)
print(LORE)
do_help()

# Базовый цикл
while hero['hp'] > 0 and not artifact:
    action = input('Вы в главном меню: \n')
    if action.capitalize() not in commands:
        print(error_text)
    if action.lower() == 'выход' or action.lower() == 'exit' or action.lower() == 'quit':
        print(game_exit)
        break
    elif action.lower() == 'помошь' or action.lower() == 'help':
        do_help()
    elif action.lower() == 'статистика' or action.lower() == 'stats':
        stats(hero)
    elif action.lower() == 'старт' or action.lower() == 'start':
        artifact = start(hero, enemies)

if hero['hp'] <= 0:
    print('Вы проиграли.')
elif artifact:
    print(
        'Вы получили артефакт "Великих". '
        'Теперь вы обладаете невероятной силой.\n'
        'Используйте её на восстановление справедливости!')
else:
    print('Вы прервали игру\n')
