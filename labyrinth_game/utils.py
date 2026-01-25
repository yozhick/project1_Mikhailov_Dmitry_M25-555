from labyrinth_game.constants import ROOMS
import math

def describe_current_room(game_state: dict) -> None:
    current_room_name = game_state['current_room']
    current_room = ROOMS[current_room_name]

    print(f'=={current_room_name.upper()}==')
    print(current_room['description'])

    items = current_room['items']
    if items:
        print('Заметные предметы:', ', '.join(items))

    exits = current_room['exits']
    if exits:
        print('Выходы:', ', '.join(exits.keys()))

    puzzle = current_room['puzzle']
    if puzzle:
        print('Кажется, здесь есть загадка (используйте команду solve).')

def solve_puzzle(game_state: dict) -> None:
    current_room_name = game_state['current_room']
    if current_room_name == 'treasure_room':
        attempt_open_treasure(game_state)
        return
    current_room = ROOMS[current_room_name]
    puzzle = current_room['puzzle']
    if not puzzle:
        print('Загадок здесь нет.')
        return
    question = puzzle["question"]
    correct_answers = { possible_answer.strip().lower() for possible_answer in puzzle["answers"] }
    print(question)
    user_answer = get_input('Ваш ответ: ').strip().lower()
    if user_answer in correct_answers:
        print('Верно! Загадка решена.')
        reward = puzzle["reward"]
        if reward:
            game_state["player_inventory"].append(reward)
            print("Вы получили награду:", reward)
            puzzle["reward"] = None
    else:
        if current_room_name == "trap_room":
            print('Неправильный ответ вызывает срабатывание ловушки...')
            trigger_trap(game_state)
        else:
            print('Неверно. Попробуйте снова.')

def attempt_open_treasure(game_state: dict) -> None:
    current_room_name = game_state['current_room']
    current_room = ROOMS[current_room_name]
    if 'treasure_key' in game_state['player_inventory']:
        print('Вы применяете ключ, и замок щёлкает. Сундук открыт!')
        if 'treasure_chest' in current_room['items']:
            current_room['items'].remove('treasure_chest')
        print('В сундуке сокровище! Вы победили!')
        game_state['game_over'] = True
        return
    answer = input("Сундук заперт... Ввести код? (да/нет): ").strip().lower()
    if answer != "да":
        print("Вы отступаете от сундука.")
        return
    code = get_input("Введите код: ")
    puzzle = current_room["puzzle"]
    if puzzle is None:
        print("Здесь нет кода для взлома.")
        return
    _, correct_code = puzzle
    if code == correct_code:
        print("Код верный. Сундук открыт!")
        if "treasure_chest" in current_room["items"]:
            current_room["items"].remove("treasure_chest")
        print("В сундуке сокровище! Вы победили!")
        game_state["game_over"] = True
    else:
        print("Неверный код.")

def get_input(prompt: str = '> ') -> str:
    try:
        return input(prompt)
    except (KeyboardInterrupt, EOFError):
        print('\nВыход из игры.')
        return 'quit'

def pseudo_random(seed: int, modulo: int) -> int:
    x = math.sin(seed * 12.9898) * 43758.5453
    fractional_part = x - math.floor(x)
    return int(fractional_part * modulo)

def trigger_trap(game_state: dict) -> None:
    print("Ловушка активирована! Пол стал дрожать...")
    inventory = game_state["player_inventory"]
    if inventory:
        item_index = pseudo_random(game_state["steps_taken"], len(inventory))
        lost_item = inventory.pop(item_index)
        print("Вы потеряли предмет:", lost_item)
        return
    damage_roll = pseudo_random(game_state["steps_taken"], 10)  # 0..9
    if damage_roll < 3:
        print("Ловушка нанесла смертельный урон. Вы проиграли!")
        game_state["game_over"] = True
    else:
        print("Вы получили урон, но уцелели.")

def random_event(game_state: dict) -> None:
    event_roll = pseudo_random(game_state["steps_taken"], 10)
    if event_roll != 0:
        return
    event_type = pseudo_random(game_state["steps_taken"] + 1, 3)
    current_room_name = game_state["current_room"]
    current_room = ROOMS[current_room_name]
    match event_type:
        case 0:
            print("Вы замечаете на полу монетку.")
            current_room["items"].append("coin")
        case 1:
            print("Вы слышите шорох рядом...")
            if "sword" in game_state["player_inventory"]:
                print("Вы выхватываете меч - существо отступает!")
        case 2:
            if current_room_name == "trap_room" and "torch" not in game_state["player_inventory"]:
                print("Становится слишком темно... вы чувствуете опасность!")
                trigger_trap(game_state)

def show_help(commands: dict) -> None:
    print("\nДоступные команды:")
    for command, description in commands.items():
        print(f"  {command:<16}  - {description}")

