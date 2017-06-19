#Samira Mantri 2/26/16 section:3 MantriSamira_assign4_part2.py

while True:
    #ask the user how many sticks the user wants in the game
    sticks=int(input("How many sticks (10-100) "))
    #make sure the number of sticks are within the given range
    if sticks>=10 and sticks<=100:
         break
    else:
        #If there are too few sticks tell the user to try again
        if sticks<10:
            print("Sorry, that's too few sticks. Try again.")
        #If there are too many sticks tell the user to try again
        else:
            print("Sorry, that's too many sticks. Try again.")
               
#If the number of sticks chosen are within the given range, let the user know the game will commence
print("Great! Let's play ...")
print()

player=0
while True:
    #indicate which player is up
    player+=1
    if player%2:
        print("Turn: Player 1")
    else:
        print("Turn: Player 2")
    #tell the user how many sticks are on the table
    if sticks>1:
        print("There are", sticks,"sticks on the table.")
    else:
        print("There is",sticks,"stick on the table.")
    #ask the user how many sticks they want to take
    choice=int(input("How many sticks do you want to take (1, 2, or 3)? "))
    #make sure the number of sticks the user takes is valid
    if choice==1 or choice==2 or choice==3:
        #ensure the user can't take more sticks than is on the table
        if choice>sticks:
            print("Sorry, that's not a valid number.")
            player-=1
            print()
        else:
            #Make sure the number of sticks taken is subtracted from the total
            #number of sticks still on the table
            sticks-=choice
            print()
            #only when there are no sticks on the table can the game end
            if sticks==0:
                #Indicate who won the game based on who picked up the last stick
                if player%2:
                    print("There are no sticks left on the table! Game over.")
                    print("Player 2 wins!")
                    break
                else:
                    print("There are no sticks left on the table! Game over.")
                    print("Player 1 wins!")
                    break
                
    #if the number of sticks is not a valid number, prompt the user
    #to enter how many sticks they want to take again
    else:
        print("Sorry, that's not a valid number.")
        player-=1
        print()


        
    









