Correctnumbers = 3
userGuess = 0
while userGuess != Correctnumbers:
    userGuess = int(input("Please guess a number :"))
    if userGuess > Correctnumbers:
        print("Too Large")
    elif userGuess < Correctnumbers:
        print("Too Small")
    elif userGuess == Correctnumbers:
        print("This CorrectNumber")