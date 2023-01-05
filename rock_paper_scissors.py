def play():
    # Due to the maximum recursion rule of python, it is preferable to use a while loop for a piece of code that
    # might repeat rather than recursively calling the same function from within the function
    # While you may think "no fool would make 1000 mistakes in a row" don't underestimate the ingenuity of fools
    # Although this code forms a recursion between the play() and again() functions if the game is played enough times
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
            again()
        else:
            print("only 'rock', 'paper' and 'scissors' are valid options")
            continue


def again():
    while True:
        x = input("would you like to play again? (Y/N):").lower()
        if x == 'y':
            play()
        elif x == 'n':
            break
        else:
            print("only 'y' and 'n' are valid options")
            continue


play()
