import string
import random

players = ["Mary", "bot"]


def prompt_initial_pencils():
    def is_invalid(text):
        for c in list(text):
            if c not in string.digits:
                print('The number of pencils should be numeric')
                return True
        if text == "0":
            print('The number of pencils should be positive')
            return True
        return False

    user_input = input("How many pencils would you like to use:\n")
    while is_invalid(user_input):
        user_input = input()
    return int(user_input)


def prompt_turn_pencils():
    def is_invalid(text):
        if text not in ['1', '2', '3']:
            print("Possible values: '1', '2' or '3'")
            return True
        if int(text) > pencil_count:
            print('Too many pencils were taken')
            return True
        return False

    user_input = input()
    while is_invalid(user_input):
        user_input = input()
    return int(user_input)


def bot_strategy():
    if pencil_count % 4 == 1:
        turn_count = min(pencil_count, random.randint(1, 3))
    else:
        turn_count = (pencil_count - 1) % 4
    print(turn_count)
    return turn_count


def do_turn():
    global pencil_count, turn_player
    print('|' * pencil_count)
    print(f"{turn_player}'s turn!")
    if turn_player == "bot":
        pencil_count -= bot_strategy()
    else:
        pencil_count -= prompt_turn_pencils()
    turn_player = players[1] if turn_player == players[0] else players[0]
    if pencil_count == 0:
        print(f'{turn_player} won!')


pencil_count = prompt_initial_pencils()
turn_player = input(f'Who will be the first ({players[0]}, {players[1]}):\n')
while turn_player not in players:
    print(f'Choose between {players[0]} and {players[1]}!')
    turn_player = input()

while pencil_count > 0:
    do_turn()
