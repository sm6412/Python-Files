#Samira Mantri 2/15/16 section:3 MantriSamira_assign3_problem3.py

#Create an input that asks the user for a month number
#Make this answer an integer for later calculations
month=int(input("Enter a month (1-12): "))

#Create an input that asks the user for the day number
day=int(input("Enter a day (1-31): "))

#Use boolean expressions and variables to make month numbers represent the name of the month
if month==1:
    month_name='January'
if month==2:
    month_name='Febuary'
if month==3:
    month_name='March'
if month==4:
    month_name='April'
if month==5:
    month_name='May'
if month==6:
    month_name='June'
if month==7:
    month_name='July'
if month==8:
    month_name='August'
if month==9:
    month_name='September'
if month==10:
    month_name='October'
if month==11:
    month_name='November'
if month==12:
    month_name='December'

#Use boolean expressions to make sure the month and date are both valid
#First check the month
if month>12:
    print("That's not a valid date!")
elif month<1:
    print("That's not a valid date!")
else:
    #Make sure the day during the month is also valid
    if month==1:
        if day>31 or day<1:
            print("That's not a valid date!")
        else:
            #Make sure to indicate that dates before Jan 25th are before the semester starts
            if day<25:
                print(month_name,day,"is before the start of the Spring 2016 term.")
            else:
                print(month_name,day,"is not a holiday at NYU. The university is open.")
    #Make sure the day during the month is also valid
    elif month==2:
        if day>29 or day<1:
            print("That's not a valid date!")
        else:
            #Feb 15th is President's day so NYU will not be open
            if day==15:
                print(month_name,day,"is President's day. NYU is not open on this day.")
            else:
                print(month_name,day,"is not a holiday at NYU. The university is open.")
    #Make sure the day during the month is also valid
    elif month==3:
        if day>31 or day<1:
            print("That's not a valid date!")
        else:
            #March 14-20 is Spring Break so make sure to indicate that NYU will not be open
            if day>=14 and day<=20:
                print(month_name,day,"is during Spring Break. NYU is not open on this day.")
            else:
                print(month_name,day,"is not a holiday at NYU. The university is open.") 
    #Make sure the day during the month is also valid
    elif month==4:
        if day>30 or day<1:
            print("That's not a valid date!")
        else:
            print(month_name,day,"is not a holiday at NYU. The university is open.")
    #Make sure the day during the month is also valid
    elif month==5:
        if day>31 or day<1:
            print("That's not a valid date!")
        else:
            #On and before May 9th have classes
            if day<=9:
                print(month_name,day,"is not a holiday at NYU. The university is open.")
            #Anyting after May 9th is after the end of the semester 
            else:
                print(month_name,day,"is after the end of the Spring 2016 term.")
    #Make sure the day during the month is also valid
    elif month==6:
        if day>30 or day<1:
            print("That's not a valid date!")
        #Anyting after May 9th is after the end of the semester
        else:
            print(month_name,day,"is after the end of the Spring 2016 term.")
    #Make sure the day during the month is also valid
    elif month==7:
        if day>31 or day<1:
            print("That's not a valid date!")
        #Anyting after May 9th is after the end of the semester
        else:
            print(month_name,day,"is after the end of the Spring 2016 term.")
    #Make sure the day during the month is also valid
    elif month==8:
        if day>31 or day<1:
            print("That's not a valid date!")
        #Anyting after May 9th is after the end of the semester
        else:
            print(month_name,day,"is after the end of the Spring 2016 term.")
    #Make sure the day during the month is also valid
    elif month==9:
        if day>30 or day<1:
            print("That's not a valid date!")
        #Anyting after May 9th is after the end of the semester
        else:
            print(month_name,day,"is after the end of the Spring 2016 term.")
    #Make sure the day during the month is also valid
    elif month==10:
        if day>31 or day<1:
            print("That's not a valid date!")
        #Anyting after May 9th is after the end of the semester
        else:
            print(month_name,day,"is after the end of the Spring 2016 term.")
    #Make sure the day during the month is also valid
    elif month==11:
        if day>30 or day<1:
            print("That's not a valid date!")
        #Anyting after May 9th is after the end of the semester
        else:
            print(month_name,day,"is after the end of the Spring 2016 term.")
    #Make sure the day during the month is also valid
    else:
        if day>31 or day<1:
            print("That's not a valid date!")
        #Anyting after May 9th is after the end of the semester
        else:
            print(month_name,day,"is after the end of the Spring 2016 term.")
       
    
   
    
