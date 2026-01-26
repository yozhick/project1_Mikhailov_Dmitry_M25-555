# labyrinth_game/constants.py
ROOMS = {
    'entrance': {
        'description': (
            'Вы в темном входе лабиринта. Стены покрыты мхом. '
            'На полу лежит старый факел.'
        ),
        'exits': {'north': 'hall', 'east': 'trap_room', 'west': 'kitchen'},
        'items': ['torch'],
        'puzzle': None,
    },
    'hall': {
        'description': (
            'Большой зал с эхом. По центру стоит пьедестал '
            'с запечатанным сундуком.'
        ),
        'exits': {
            'south': 'entrance',
            'west': 'library',
            'north': 'treasure_room',
            'east': 'toilet',
        },
        'items': [],
        'puzzle': {
            'question': (
                'На пьедестале надпись: "Назовите число, которое идет после девяти". '
                'Введите ответ цифрами.'
            ),
            'answers': {'10', 'десять'},
            'reward': 'coin',
        },
    },
    'trap_room': {
        'description': (
            'Комната с хитрой плиточной поломкой. На стене видна надпись: '
            '"Осторожно — ловушка".'
        ),
        'exits': {'west': 'entrance'},
        'items': ['rusty_key'],
        'puzzle': {
            'question': (
                'Система плит активна. Чтобы пройти, назовите слово "шаг" '
                'три раза подряд (введите "шаг шаг шаг")'
            ),
            'answers': {'шаг шаг шаг'},
            'reward': 'bandage',
        },
    },
    'library': {
        'description': (
            'Пыльная библиотека. На полках старые свитки. '
            'Где-то здесь может быть ключ от сокровищницы.'
        ),
        'exits': {'east': 'hall', 'north': 'armory'},
        'items': ['ancient_book'],
        'puzzle': {
            'question': (
                'В одном свитке загадка: "Что растет, когда его съедают?" '
                '(ответ одно слово)'
            ),
            'answers': {'пространство'},
            'reward': 'map_fragment',
        },
    },
    'armory': {
        'description': (
            'Старая оружейная комната. На стене висит меч, рядом — '
            'небольшая бронзовая шкатулка.'
        ),
        'exits': {'south': 'library'},
        'items': ['sword', 'bronze_box'],
        'puzzle': None,
    },
    'treasure_room': {
        'description': (
            'Комната, на столе большой сундук. Дверь заперта — '
            'нужен особый ключ.'
        ),
        'exits': {'south': 'hall'},
        'items': ['treasure_chest'],
        'puzzle': {
            'question': (
                'Дверь защищена кодом. Введите код (подсказка: это число '
                'пятикратного шага, 2*5= ? )'
            ),
            'answers': {'10', 'десять'},
            'reward': None,
        },
    },
    'toilet': {
        'description': 'Просто немного передохните...',
        'exits': {'west': 'hall'},
        'items': [],
        'puzzle': {
            'question': 'Не забудьте смыть за собой (введите "смыть").',
            'answers': {'смыть'},
            'reward': 'toilet_paper',
        },
    },
    'kitchen': {
        'description': (
            'Кухня. На столе холодный суп, в углу ведро. '
            'Кто-то явно тут жил.'
        ),
        'exits': {'east': 'entrance'},
        'items': ['knife', 'bread'],
        'puzzle': {
            'question': 'На стене: "Сначала руки". Введите "мыть".',
            'answers': {'мыть'},
            'reward': 'soap',
        },
    },
}

COMMANDS = {
    'go <direction>': 'перейти в направлении (north/south/east/west)',
    'look': 'осмотреть текущую комнату',
    'take <item>': 'поднять предмет',
    'use <item>': 'использовать предмет из инвентаря',
    'inventory': 'показать инвентарь',
    'solve': 'попытаться решить загадку в комнате',
    'quit': 'выйти из игры',
    'help': 'показать это сообщение',
}

EVENT_PROBABILITY = 10
EVENT_TRIGGER_VALUE = 0
EVENT_TYPE = 3
TRAP_DAMAGE = 10
TRAP_DEATH_THRESHOLD = 3  # < 3 -> смерть
HELP_COMMAND_COLUMN_WIDTH = 16
