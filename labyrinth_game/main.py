#!/usr/bin/env python3

import labyrinth_game.constants as constants
import labyrinth_game.player_actions as actions
import labyrinth_game.utils as utils

game_state = {
    'player_inventory': [],  # Инвентарь игрока
    'current_room': 'entrance',  # Текущая комната
    'game_over': False,  # Значения окончания игры
    'steps_taken': 0  # Количество шагов
}

def process_command(game_state: dict, command: str) -> None:
    """Обработка введённой пользователем строки."""
    parts = command.strip().split(maxsplit=1)
    cmd = parts[0].lower() if parts else ""
    arg = parts[1].strip() if len(parts) == 2 else ""
    match cmd:
        case "north" | "south" | "east" | "west":
            if arg:
                print("Лишний аргумент. Пример: north")
                return
            actions.move_player(game_state, cmd)
        case "look":
            utils.describe_current_room(game_state)
        case "go":
            if not arg:
                print("Куда идти? Пример: go north")
                return
            actions.move_player(game_state, arg)
        case "take":
            if not arg:
                print("Что взять? Пример: take torch")
                return
            actions.take_item(game_state, arg)
        case "inventory":
            inv = game_state["player_inventory"]
            if inv:
                print("Инвентарь:", ", ".join(inv))
            else:
                print("Инвентарь пуст.")
        case "use":
            if not arg:
                print("Что использовать? Пример: use torch")
                return
            actions.use_item(game_state, arg)
        case "solve":
            utils.solve_puzzle(game_state)
        case "quit" | "exit":
            game_state["game_over"] = True
        case "help" | "?":
            utils.show_help(constants.COMMANDS)
        case "":
            return
        case _:
            print("Неизвестная команда.")

def main():
    """Точка входа: приветствие, стартовое описание комнаты и основной цикл."""
    print("Добро пожаловать в Лабиринт сокровищ!")
    utils.describe_current_room(game_state)
    while not game_state["game_over"]:
        player_command = utils.get_input()
        process_command(game_state, player_command)

if __name__ == "__main__":
    main()