import random

# range computer can choose to have user guess
ranNumber = random.randint(1, 20)

# welkoming message
Welcom_msg = print(
    "welcom to the guessing game would you try and guess the random number. ")

# function that runs how many time a user can guess number.


def num_tries():
    global numGuess
    userguess = 0
    ranNumber = random.randint(1, 20)
    print("Try you luck :")

    while userguess < 4:
        print("enter your guess now : ")
        numGuess = input()
        numGuess = int(numGuess)

        userguess += 1

        if numGuess < ranNumber:
            print("You are a bit too Low")

        if numGuess > ranNumber:
            print("you are a bit too High")

        if numGuess == ranNumber:
            break
    if numGuess == ranNumber:
        userguess = str(userguess)
        print("Graet you have guessed it correctly")
    if numGuess != ranNumber:
        ranNumber = str(ranNumber)
        print("Sorry, Did not get it this time. Please try again")
        print(Welcom_msg)
        cont = input("Do you want to continue? Y = yes, N = no")

        if cont == "Y":
            print(num_tries())
        else:
            print("Thanks for trying")


print(num_tries())
