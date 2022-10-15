players = ["Mary", "Joseph"]


def prompt_pencil_count(prompt_text):
    return int(input(prompt_text))


def prompt_turn_player():
    return input(f'Who will be the first ({players[0]}, {players[1]}):\n')


def do_turn():
    global pencil_count, turn_player
    print('|' * pencil_count)
    print(f"{turn_player}'s turn")
    pencil_count -= prompt_pencil_count("")
    turn_player = players[1] if turn_player == players[0] else players[0]


pencil_count = prompt_pencil_count("How many pencils would you like to use:\n")
turn_player = prompt_turn_player()
while turn_player not in players:
    print(f'Choose either {players[0]} or {players[1]}!')
    turn_player = prompt_turn_player()

while pencil_count > 0:
    do_turn()
