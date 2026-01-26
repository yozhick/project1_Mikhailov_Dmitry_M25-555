import labyrinth_game.utils as utils
from labyrinth_game.constants import ROOMS


def show_inventory(game_state: dict) -> None:
    """Печатает содержимое инвентаря игрока из game_state."""
    inventory = game_state['player_inventory']
    if inventory:
        print(', '.join(inventory))
    else:
        print('Инвентарь пуст.')

def move_player(game_state: dict, direction: str) -> None:
    """Перемещает игрока в указанном направлении."""
    current_room_name = game_state['current_room']
    current_room = ROOMS[current_room_name]
    exits = current_room['exits']
    if direction not in exits:
        print("Нельзя пойти в этом направлении.")
        return
    next_room_name = exits[direction]
    if next_room_name == 'treasure_room':
        if 'rusty_key' not in game_state['player_inventory']:
            print('Дверь заперта. Нужен ключ, чтобы пройти дальше.')
            return
        else:
            print(
                'Вы используете найденный ключ, '
                'чтобы открыть путь в комнату сокровищ.'
            )
    game_state['current_room'] = next_room_name
    game_state['steps_taken'] = game_state['steps_taken'] + 1
    utils.describe_current_room(game_state)
    utils.random_event(game_state)

def take_item(game_state: dict, item_name: str) -> None:
    """Подбирает предмет из текущей комнаты."""
    if item_name == 'treasure_chest':
        print('Вы не можете поднять сундук, он слишком тяжелый.')
        return
    current_room_name = game_state['current_room']
    current_room = ROOMS[current_room_name]
    items = current_room['items']
    if item_name in items:
        items.remove(item_name)
        game_state['player_inventory'].append(item_name)
        print('Вы подняли:', item_name)
    else:
        print('Такого предмета здесь нет.')

def use_item(game_state: dict, item_name: str) -> None:
    """Использует указанный предмет из инвентаря."""
    inventory = game_state['player_inventory']
    if item_name not in inventory:
        print('У вас нет такого предмета.')
        return
    match item_name:
        case 'torch':
            print('Факел вспыхивает ярче. Стало светлее.')
        case 'sword':
            print('Вы сжимаете меч. Уверенность возвращается.')
        case 'bronze_box':
            print('Вы открываете бронзовую шкатулку.')
            if 'rusty_key' not in inventory:
                inventory.append('rusty_key')
                print('Внутри вы нашли: rusty_key')
        case "bread":
            print("Вы ломаете хлеб... внутри что-то звякает.")
            inventory.remove("bread")
            inventory.append("bread_leftovers")
            if "treasure_key" not in inventory:
                inventory.append("treasure_key")
                print("Вы нашли: treasure_key")
        case _:
            print('Вы не знаете, как использовать этот предмет.')
