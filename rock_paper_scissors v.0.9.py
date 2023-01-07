"""Due to the maximum recursion rule of python, it is preferable to use a while loop for a piece of code that
might repeat rather than recursively calling the same function from within the function
While you may think "no fool would make 1000 mistakes in a row" don't underestimate the ingenuity of fools
This code forms circular recursion between the play() and again() functions if the game is played enough times"""


def play():
    x = input("Player1: rock, paper or scissors?:")
    y = input("Player2: rock, paper or scissors?:")
    if not validate((x.lower(), y.lower())):
        play()
    else:
        evaluate((x.lower(), y.lower()))


def validate(x):
    if len(set(x).intersection({'rock', 'paper', 'scissors'})) == 0:
        print("only rock, paper and scissors are valid options")
        return False
    else:
        return True


def evaluate(x):
    if len(set(x).intersection({'rock', 'paper'})) == 2:
        print("paper defeats rock")
    elif len(set(x).intersection({'rock', 'scissors'})) == 2:
        print("rock defeats scissors")
    elif len(set(x).intersection({'paper', 'scissors'})) == 2:
        print("scissors defeats paper")
    else:
        print("it's a draw")
    again()


def again():
    x = input("would you like yo play again? (Y/N):")
    if x.lower() == 'y':
        play()
    elif x.lower() == 'n':
        return
    else:
        print("only 'y' and 'n' are valid options")
        again()


play()
