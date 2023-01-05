"""In an attempt to get rid of circular recursion, I attempted ot implement while loops, although I was not able to
integrate the again() function into the main body of the code
Also there is a mechanic regarding breaking a while loop where I don't follow the logic (section commented)
"""


def play():
    while True:
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
            break
        else:
            print("only 'rock', 'paper' and 'scissors' are valid options")
            continue
    again()


def again():
    while True:
        x = input("would you like to play again? (Y/N):").lower()
        if x == 'y':
            play()
            break
            # If this break statement is not here, and the game is played multiple times by pressing "y", if you
            # then want to stop playing by pressing "n", you will be re-prompted to play again as many times as games
            # played before. Almost like some recursion is being resolved. I don't understand why
        elif x == 'n':
            break
        else:
            print("only 'y' and 'n' are valid options")
            continue

#test
play()
