#Samira Mantri 2/22/16 section=3 MantriSamira_assign4_program1.py

#import random
import random

#Use a loop to ensure that the sides on the dice are valid
while True:
    #Ask the user how many sides they want their die to have
    sides=int(input("How many sides on your dice (4, 6, 8, 10, 12, or 20)? "))
    if sides==4 or sides==6 or sides==8 or sides==10 or sides==12 or sides==20:
        print()
        print("Thanks! Here we go ...")
        print()
        break
      
    else:
        print("Sorry, that's not a valid size.")
        print()


#Set initial roll equal to one
roll=1
#set the initial number of doubles rolls equal to one
doubles_roll=1
#set the first die roll equal to zero
die1_roll=0
#set the second die roll equal to zero
die2_roll=0
while True:
   #Use the random module to randomly pick a number that is on the particular die
    if sides==4:
            die1=random.randint(1,4)
            die2=random.randint(1,4)
    elif sides==6:
            die1=random.randint(1,6)
            die2=random.randint(1,6)
    elif sides==8:
            die1=random.randint(1,8)
            die2=random.randint(1,8)
    elif sides==10:
            die1=random.randint(1,10)
            die2=random.randint(1,10)
    elif sides==12:
            die1=random.randint(1,12)
            die2=random.randint(1,12)
    elif sides==20:
            die1=random.randint(1,20)
            die2=random.randint(1,20)
    #format roll number so it is followed by a period
    str_roll=str(roll)
    format_roll=str_roll+"."
    #display die numbers and their roll number
    print(format_roll,"die number 1 is",die1,"and die number 2 is",die2)
    print()
   #Check to see if snake eyes is rolled
    if die1==1 and die2==1:
        #Make sure the congratulatory statements make sense
        if roll==1:
            print("You got snake eyes! On try number",roll)
        else:
            print("You got snake eyes! Finally! On try number",roll)
        #Calculate the percentage of the rolls that were doubles
        percent_doubles_roll=(doubles_roll/roll)*100
        #Make sure answer is to 2 decimal places
        format_percent_doubles_roll=format(percent_doubles_roll,".2f")
        #Make sure the percent mark is attached to the percentage of rolls that produced doubles
        string_doubles_roll=str(format_percent_doubles_roll)
        final_doubles_roll="("+string_doubles_roll+"%"
        #tell the user how many times they rolled doubles and the percentage of rolls that produced doubles
        if doubles_roll==1:
            print("Along the way you rolled doubles",doubles_roll,"time",final_doubles_roll,"of all rolls were doubles)")
        else:
            print("Along the way you rolled doubles",doubles_roll,"times",final_doubles_roll,"of all rolls were doubles)")
        #Determine what the average roll of die 1 was
        avg_of_die1=(die1_roll+die1)/roll
        format_avg_of_die1=format(avg_of_die1,".2f")
        print("The average roll for die #1 was",format_avg_of_die1)
        #Determine what the average roll of die 2 was
        avg_of_die2=(die2_roll+die2)/roll
        format_avg_of_die2=format(avg_of_die2,".2f")
        print("The average roll for die #2 was",format_avg_of_die2)
        break
    #if snake eyes are not rolled on the first try, loop should continue
    else:
        #keep track of the rolls
        roll+=1
        #keep track of if the user rolls doubles
        if die1==die2:
            doubles_roll+=1
        #keep track of the sum of die one rolls
        die1_roll+=die1
        #keep track of the sum of die two rolls
        die2_roll+=die2
    

   
        
        

    


