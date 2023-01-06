""""rock/paper/scissors version without any circular recursion and with what seems to me decently understandable
code"""


def play():
    choices = {"player 1": input("Player1: rock, paper or scissors?:").lower()}
    choices.update({"player 2": input("Player2: rock, paper or scissors?:").lower()})
    if validate(choices) == "not valid":
        return True
    else:
        evaluate(choices)
    if again() == "again":
        return True
    else:
        return False


def validate(choices):
    valid = ['rock', 'paper', 'scissors']
    if choices["player 1"] in valid and choices["player 2"] in valid:
        return
    else:
        print("only rock, paper and scissors are valid options")
        return "not valid"


def evaluate(choices):
    player = {v: k for k, v in choices.items()}
    if len({choices["player 1"], choices["player 2"]}.intersection({'rock', 'paper'})) == 2:
        print(f"paper defeats rock, {player['paper']} wins")
    elif len({choices["player 1"], choices["player 2"]}.intersection({'rock', 'scissors'})) == 2:
        print(f"rock defeats scissors, {player['rock']} wins")
    elif len({choices["player 1"], choices["player 2"]}.intersection({'paper', 'scissors'})) == 2:
        print(f"scissors defeats paper, {player['scissors']} wins")
    else:
        print("it's a draw")


def again():
    while True:
        replay = input("would you like to play again? (Y/N):").lower()
        if replay == 'y':
            return "again"
        elif replay == 'n':
            return
        else:
            print("only 'y' and 'n' are valid options")
            continue


while play():
    pass
