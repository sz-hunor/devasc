def play():
    x = input("Player1: rock, paper or scissors?:")
    y = input("Player2: rock, paper or scissors?:")
    if not validate((x.lower(), y.lower())):
        play()
    else:
        evaluate((x.lower(), y.lower()))


def validate(x):
    if len(set(x).intersection({'rock', 'paper', 'scissors'})) == 0:
        print ("only rock, paper and scissors are valid options")
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
