"""this seems to work generally, but it uses circular recursion by calling the different functions from each other
in a circular manner"""


def play():
    x = {"player 1": input("Player1: rock, paper or scissors?:").lower()}
    x.update({"player 2": input("Player2: rock, paper or scissors?:").lower()})
    valid = ['rock', 'paper', 'scissors']
    if x["player 1"] in valid and x["player 2"] in valid:
        y = {v: k for k, v in x.items()}
        if len({x["player 1"], x["player 2"]}.intersection({'rock', 'paper'})) == 2:
            print(f"paper defeats rock, {y['paper']} wins")
        elif len({x["player 1"], x["player 2"]}.intersection({'rock', 'scissors'})) == 2:
            print(f"rock defeats scissors, {y['rock']} wins")
        elif len({x["player 1"], x["player 2"]}.intersection({'paper', 'scissors'})) == 2:
            print(f"scissors defeats paper, {y['scissors']} wins")
        else:
            print("it's a draw")
        again()
    else:
        print("only 'rock', 'paper' and 'scissors' are valid options")
        play()


def again():
    x = input("would you like yo play again? (Y/N):").lower()
    if x == 'y':
        play()
    elif x == 'n':
        return
    else:
        print("only 'y' and 'n' are valid options")
        again()


play()
