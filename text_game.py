# Програма полностью работает без {bright_blue}, {color_end}
# Если вместо цвета у вас выводится набор символов, поменяйть строки 7 и 8 на
# bright_blue = '' и color_end = ''

# Системное (Работает только в PyCharm)

yellow = '\x1b[1;92m'
dark_blue = '\x1b[1;94m'
pink = '\x1b[1;95m'
bright_blue = '\x1b[1;4;96m'
grey = '\x1b[1;97m'
color_end = '\x1b[0m'

# Функции


def stats(person):
    statistics = \
        f'|{"Имя":^{len(person["name"]) + 4}}|' \
        f'{"Броня":^7}|' \
        f'{"Урон":^6}|' \
        f'{"Здоровье":^10}|\n' \
        f'|{bright_blue}{person["name"]:^{len(person["name"]) + 4}}{color_end}|' \
        f'{bright_blue}{person["armor"]:^7}{color_end}|' \
        f'{bright_blue}{person["damage"]:^6}{color_end}|' \
        f'{bright_blue}{person["hp"]:^10}{color_end}|'
    print(statistics)
    print()


def do_help():
    menu = \
        '|' + '- ' * 25 + '|\n' \
        f'|{yellow}{"Меню":^50}{color_end}|\n' \
        '|' + '- ' * 25 + '|\n'
    for i in range(len(commands)):
        menu_string = f'{bright_blue}{commands[i]}{color_end} - {yellow}{commands_desc[i]}{color_end}'
        menu += \
            f'|{menu_string:^74}|\n' \
            '|' + '- ' * 25 + '|\n'
    print(menu)


def start(h, es):
    print(
        'Привет это снова я - Дэкой. \n'
        'Ну что готов к своему первому заданию? Видишь этот склеп на вершине холма?\n'
        'В него уже на заходили 23 года. \n'
        'Говорят там завелось много чудовищь.\n'
        f'Это задание должно быть легким для тебя, еще и мешок золота от {bright_blue}Гревиаса{color_end} получишь!\n'
        f'{bright_blue}{h["name"]}{color_end} заходит в склеп и видит несколько комнат. '
        'Из каждой доносятся устрашающие звуки.\n'
        'Вы решили осматривать каждую комнату по порядку.'
    )
    fight_break = fight_all(h, es)

    return (hero['hp'] > 0) and not fight_break


def fight_all(h, es):
    i = 1
    fight_break = False
    for e in es:
        e['hp'] = e['default_hp']
        print(f'Вы заходите в {bright_blue}{i}{color_end}-ю комнату и видите в темном углу страшное существо:\n')
        stats(e)
        fight_break = fight(h, e)
        if fight_break:
            break
        i += 1

        if h['hp'] <= 0:
            print(f'Враг оказался сильнее, {bright_blue}{h["name"]}{color_end}.')
            break

        if e['hp'] <= 0:
            print(
                f'Отличный бой, {bright_blue}{h["name"]}{color_end}. '
                f'Ты победил!\n')
        do_chest(h, chest)

    return fight_break


def fight(h, e):
    is_break = False
    while e['hp'] > 0 and h['hp'] > 0:
        agree = choice_view(moves)
        if agree == 0:
            x = 'default'
        elif agree == 1:
            x = 'attack'
        elif agree == 2:
            x = 'defence'
        elif agree == 3:
            print('Вы прервали бой.')
            is_break = True
            for key, val in roles.items():
                if val['role_name'] == hero['role_name']:
                    hero.update(roles[key])
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
        print(f'Великолепный удар: Здоровье врага - {bright_blue}{e["hp"]}{color_end}, '
              f'Ваше здоровье - {bright_blue}{hero["hp"]}{color_end}')


def do_chest(h, ch):
    print(
        'Вам открылся сундук "Великих". '
        'Выберите награду.')

    if len(ch) == 0:
        print('Сундук пуст.\n')

    else:
        j = choice_view(ch)
        if ch[j] != 'оставить на следующий раз':

            if ch[j] == 'восстановить здоровье полностью':
                h['hp'] = h['max_hp']
            elif ch[j] == 'увеличить максимальное здоровье':
                h['max_hp'] *= 1.15
            elif ch[j] == 'увеличить урон':
                h['damage'] *= 1.1
            elif ch[j] == 'увеличить броню':
                h['armor'] *= 1.2
            ch.pop(j)


def choice_view(lst):
    print('Выберите')
    for i, item in enumerate(lst):
        print(f'{i} - {item}')

    while True:
        i = input('')
        if i.isdigit():
            i = int(i)
            if i < len(lst):
                return i


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
        'max_hp': 460,
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
        'default_hp': 300,
        'armor': 20,
        'damage': 80,
    },
    {
        'name': 'Heaven Vampire',
        'default_hp': 300,
        'armor': 40,
        'damage': 90,
    },
    {
        'name': 'Magical Wolf',
        'default_hp': 300,
        'armor': 60,
        'damage': 100,
     },
    {
        'name': 'Ferocious Tiger',
        'default_hp': 300,
        'armor': 80,
        'damage': 110,
     },
    {
        'name': 'Risen Guard',
        'default_hp': 300,
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
    'оставить на следующий раз'
]

commands = (
    'Start',
    'Stats',
    'Help',
    'Exit',
)

commands_desc = (
    'Начать задание',
    'Статистика',
    'Помощь',
    'Выход',
)

instructor = {
    'hp': 1000,
    'armor': 100,
}

moves = [
    'Стандарт',
    f'Атака ({move_rules["attack"]["damage_kf"]}x урон и {move_rules["attack"]["armor_kf"]}x броня)',
    f'Защита ({move_rules["defence"]["damage_kf"]}x урон и {move_rules["defence"]["armor_kf"]}x броня)',
    'Прервать бой',
]
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
    f"Здравствуй, {hero_class} {bright_blue}{hero['name']}{color_end}!\n" \
    f"Меня зовут {bright_blue}Дэкой{color_end}. " \
    "Даже не знаю как ты тут оказался, но мы тебе рады. " \
    "Я расскажу тебе о наших краях. "

error_text = \
    'Неизвестная команда. ' \
    f'Ознакомиться с списоком возможных команд можно введя {bright_blue}Help{color_end}'

LORE = f'Ты попали в {bright_blue}Вальтсардию{color_end}. \n' \
       'Это маленькое королевство людей с богатой историей. \n' \
       f'В нем есть 2 крупных города {bright_blue}Верхейм{color_end} и {bright_blue}Рейнварден{color_end}. \n' \
       'Добро пожаловать!\n'

INTRO = \
    'Я вижу, что ты боец. ' \
    f'Предлагаю тебе устроить спарринг с моим другом {bright_blue}Фриском{color_end}'

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
