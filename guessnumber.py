print("Please think of a number between 0 and 100!")

feedback = ""
upper = 100
lower = 0
guess = 0

while feedback != "c":
    guess = int((upper + lower)/2)
    print("Is your secret number " + str(guess) + "?")
    feedback = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if feedback == "h":
        upper = guess
    elif feedback == "l":
        lower = guess
    elif feedback == "c":
        pass
    else:
        print("Sorry, I did not understand your input.")
print("Game over. Your secret number was " + str(guess) + ".")