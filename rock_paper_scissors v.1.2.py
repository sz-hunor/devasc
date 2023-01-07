""""rock/paper/scissors version without any circular recursion and with what seems to me decently understandable
code"""


def rock_paper_scissors():
    choices = {}
    choices.update({"player 1": input("Player1: rock, paper or scissors?:").lower()})
    choices.update({"player 2": input("Player2: rock, paper or scissors?:").lower()})
    if invalid_choices(choices):
        return True
    else:
        declare_winner(choices)
        return new_game()


def invalid_choices(choices):
    valid = ['rock', 'paper', 'scissors']
    if choices["player 1"] in valid and choices["player 2"] in valid:
        return False
    else:
        print("only rock, paper and scissors are valid options")
        return True


def declare_winner(choices):
    player = {v: k for k, v in choices.items()}
    choices = {choices["player 1"], choices["player 2"]}
    if choices == {'rock', 'paper'}:
        print(f"paper defeats rock, {player['paper']} wins")
    elif choices == {'rock', 'scissors'}:
        print(f"rock defeats scissors, {player['rock']} wins")
    elif choices == {'paper', 'scissors'}:
        print(f"scissors defeats paper, {player['scissors']} wins")
    else:
        print("it's a draw")


def new_game():
    while True:
        replay = input("would you like to play again? (y/n):").lower()
        if replay == 'y':
            return True
        elif replay == 'n':
            return False
        else:
            print("only 'y' and 'n' are valid options")
            continue


while rock_paper_scissors():
    pass
