import string

players = ["Mary", "Joseph"]


def is_invalid(text, initial):
    if initial:
        for c in list(text):
            if c not in string.digits:
                print('The number of pencils should be numeric')
                return True
        if text == "0":
            print('The number of pencils should be positive')
            return True
    else:
        if len(text) != 1 or text[0] not in ['1', '2', '3']:
            print("Possible values: '1', '2' or '3'")
            return True
    return False


def prompt_pencil_count(initial):
    prompt = "How many pencils would you like to use:\n" if initial else ""
    user_input = input(prompt)
    while is_invalid(user_input, initial):
        user_input = input()
    return int(user_input)


def do_turn():
    global pencil_count, turn_player
    print('|' * pencil_count)
    print(f"{turn_player}'s turn!")
    user_choice = prompt_pencil_count(False)
    if user_choice > pencil_count:
        print('Too many pencils were taken')
    else:
        pencil_count -= user_choice
    if pencil_count == 0:
        print(f'{turn_player} won!')
    turn_player = players[1] if turn_player == players[0] else players[0]


pencil_count = prompt_pencil_count(True)
turn_player = input(f'Who will be the first ({players[0]}, {players[1]}):\n')
while turn_player not in players:
    print(f'Choose between {players[0]} and {players[1]}!')
    turn_player = input()

while pencil_count > 0:
    do_turn()