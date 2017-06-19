#Samira Mantri 2/14/16 section:3 MantriSamira_assign3_problem2.py

#Print a statement to let the user know between which two numbers you are guessing
print("I'm thinking of a number between 1 and 10!")

#Import the random module
import random
answer=random.randint(1,10)


#Create an input asking the user for their guess
guess=int(input("What's your guess? "))

#Use boolean data in order to tell the user they guessed correctly
if answer==guess:
    print("You got it!")
    print("The secret number was ",answer,".",sep="")
    print("It took you 1 try to guess the number.")

#Use boolean data to tell the user if they guessed too high or too low
#Then make sure to set up another input so they can guess again
#Ensure that they only have three guesses before the game is over

elif answer<guess:
    print("Too high, try again.")
    #repeat the process
    guess2=int(input("What's your guess? "))
    if answer==guess2:
        print("You got it!")
        print("The secret number was ",answer,".",sep="")
        print("It took you 2 tries to guess the number.")
    elif answer<guess2:
        print("Too high try again.")
        #repeat process
        guess3=int(input("What's your guess? "))
        #Now the answer is either correct and the user wins, or they lose
        #by guessing the wrong number again. If this happens they are out
        #of guesses
        if answer==guess3:
            print("You got it!")
            print("The secret number was ",answer,".",sep="")
            print("It took you 3 tries to guess the number.")
        else:
            print("The secret number was ",answer,".",sep="")
            print("You didn't guess the number.")
    else:
        print("Too low, try again.")
        #repeat process
        guess3=int(input("What's your guess? "))
        #Now the answer is either correct and the user wins, or they lose
        #by guessing the wrong number again. If this happens they are out
        #of guesses
        if answer==guess3:
            print("You got it!")
            print("The secret number was ",answer,".",sep="")
            print("It took you 3 tries to guess the number.")
        else:
            print("The secret number was ",answer,".",sep="")
            print("You didn't guess the number.")
  

else:
    print("Too low, try again.")
    #repeat the process
    guess2=int(input("What's your guess? "))
    if answer==guess2:
        print("You got it!")
        print("The secret number was ",answer,".",sep="")
        print("It took you 2 tries to guess the number.")
    elif answer<guess2:
        print("Too high try again.")
        #repeat process
        guess3=int(input("What's your guess? "))
        #Now the answer is either correct and the user wins, or they lose
        #by guessing the wrong number again. If this happens they are out
        #of guesses
        if answer==guess3:
            print("You got it!")
            print("The secret number was ",answer,".",sep="")
            print("It took you 3 tries to guess the number.")
        else:
            print("The secret number was ",answer,".",sep="")
            print("You didn't guess the number.")
    else:
        print("Too low, try again.")
        #repeat process
        guess3=int(input("What's your guess? "))
        #Now the answer is either correct and the user wins, or they lose
        #by guessing the wrong number again. If this happens they are out
        #of guesses
        if answer==guess3:
            print("You got it!")
            print("The secret number was ",answer,".",sep="")
            print("It took you 3 tries to guess the number.")
        else:
            print("The secret number was ",answer,".",sep="")
            print("You didn't guess the number.")



    

