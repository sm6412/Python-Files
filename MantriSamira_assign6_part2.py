#Samira Mantri section-3 3/23/16 MantriSamira_assign6_part2.py

import assign6_functions

#ask user for the number of problems
while True:
    problem_num=int(input("How many problems would you like to attempt? "))
    #ensure that there are more than 0 problems 
    if problem_num>0:
        break
    else:
        print("Invalid number, try again")
        print()

#ask user for the width                    
while True:
    width=int(input("How wide do you want your digits to be? 5-10: "))
    #ensure the width is within the given range
    if width>=5 and width<=10:
        break
    else:
        print("Invalid width, try again")
        print()

#import random
import random

#Ask the user if they want to do drill mode or not
mode=input("Would you like to activate 'drill' mode? yes or no: ")

print()
print("Here we go!")
print()

#use accumulator to keep track of problem type
add=0
sub=0
mul=0
division=0

#use accumulator to keep track of attempts for different operators
add_attempts=0
sub_attempts=0
mul_attempts=0
div_attempts=0

#use accumulator to find total number of each type of problem
total_add=0
total_sub=0
total_mul=0
total_div=0

#use accumulator to keep track of questions answered right
correct_add=0
correct_sub=0
correct_mul=0
correct_div=0

#if the user types in 'yes'
if mode=="yes":
    for x in range(problem_num):
        print("What is .....")
        print()
        #randomly generate number 1, 2, 3, or 4
        symbol=random.randint(1,4)
        #use number to determine whether the operator sign
        if symbol==1:
            operator="+"
            #create a randomly generated number between 0 and 9
            num1=random.randint(0,9)
            num2=random.randint(0,9)
            add+=1
        elif symbol==2:
            operator="-"
            #create a randomly generated number between 0 and 9
            num1=random.randint(0,9)
            num2=random.randint(0,9)
            sub+=1
        elif symbol==3:
            operator="÷"
            while True:
                num1=random.randint(0,9)
                num2=random.randint(0,9)
                if num2!=0 and num1%num2==0:
                    division+=1
                    break
                else:
                    num1=0
                    num2=0
        else:
            operator="*"
            #create a randomly generated number between 0 and 9
            num1=random.randint(0,9)
            num2=random.randint(0,9)
            mul+=1

        #display the first number
        if num1==0:
            assign6_functions.number_0(width)
            print()
        elif num1==1:
            assign6_functions.number_1(width)
            print()
        elif num1==2:
            assign6_functions.number_2(width)
            print()
        elif num1==3:
            assign6_functions.number_3(width)
            print()
        elif num1==4:
            assign6_functions.number_4(width)
            print()
        elif num1==5:
            assign6_functions.number_5(width)
            print()
        elif num1==6:
            assign6_functions.number_6(width)
            print()
        elif num1==7:
            assign6_functions.number_7(width)
            print()
        elif num1==8:
            assign6_functions.number_8(width)
            print()
        else:
            assign6_functions.number_9(width)
            print()

            
        #display the operator
        if operator=="+":
            assign6_functions.plus(width)
            print()
        elif operator=="-":
            assign6_functions.minus(width)
            print()
        elif operator=="*":
            assign6_functions.multi(width)
            print()
        else:
            assign6_functions.div(width)
            print()
            

        #display the second number 
        if num2==0:
            assign6_functions.number_0(width)
            print()
        elif num2==1:
            assign6_functions.number_1(width)
            print()
        elif num2==2:
            assign6_functions.number_2(width)
            print()         
        elif num2==3:
            assign6_functions.number_3(width)
            print()
        elif num2==4:
            assign6_functions.number_4(width)
            print()
        elif num2==5:
            assign6_functions.number_5(width)
            print()
        elif num2==6:
            assign6_functions.number_6(width)
            print()
        elif num2==7:
            assign6_functions.number_7(width)
            print()
        elif num2==8:
            assign6_functions.number_8(width)
            print()
        else:
            assign6_functions.number_9(width)
            print()

        print()
        #keep drilling the user until the answer is right
        while True:
            #prompt the user for an answer
            answer=int(input("= "))
            final_answer=assign6_functions.check_answer(num1,num2,answer,operator)
            #tell the user whether their answer is correct or not
            if final_answer=="True":
                print("Correct!")
                print()
                break
            else:
                print("Sorry, that's not correct.")
                if operator=="+":
                    add_attempts+=1
                elif operator=="-":
                    sub_attempts+=1
                elif operator=="*":
                    mul_attempts+=1
                else:
                    div_attempts+=1
    print()

#if the user types in 'no'    
else:
    #use an accumulator to keep track of correct answers
    correct=0
    for x in range(problem_num):
        print("What is .....")
        print()
        #randomly generate number 1, 2, 3, or 4
        symbol=random.randint(1,4)
        #use number to determine whether the operator sign
        if symbol==1:
            operator="+"
            #create a randomly generated number between 0 and 9
            num1=random.randint(0,9)
            num2=random.randint(0,9)
            total_add+=1
        elif symbol==2:
            operator="-"
            #create a randomly generated number between 0 and 9
            num1=random.randint(0,9)
            num2=random.randint(0,9)
            total_sub+=1
        elif symbol==3:
            operator="÷"
            while True:
                num1=random.randint(0,9)
                num2=random.randint(0,9)
                if num2!=0 and num1%num2==0:
                    total_div+=1
                    break
                else:
                    num1=0
                    num2=0
        else:
            operator="*"
            #create a randomly generated number between 0 and 9
            num1=random.randint(0,9)
            num2=random.randint(0,9)
            total_mul+=1

        #display the first number
        if num1==0:
            assign6_functions.number_0(width)
            print()
        elif num1==1:
            assign6_functions.number_1(width)
            print()
        elif num1==2:
            assign6_functions.number_2(width)
            print()
        elif num1==3:
            assign6_functions.number_3(width)
            print()
        elif num1==4:
            assign6_functions.number_4(width)
            print()
        elif num1==5:
            assign6_functions.number_5(width)
            print()
        elif num1==6:
            assign6_functions.number_6(width)
            print()
        elif num1==7:
            assign6_functions.number_7(width)
            print()
        elif num1==8:
            assign6_functions.number_8(width)
            print()
        else:
            assign6_functions.number_9(width)
            print()

            
        #display the operator
        if operator=="+":
            assign6_functions.plus(width)
            print()
        elif operator=="-":
            assign6_functions.minus(width)
            print()
        elif operator=="*":
            assign6_functions.multi(width)
            print()
        else:
            assign6_functions.div(width)
            print()
            

        #display the second number 
        if num2==0:
            assign6_functions.number_0(width)
            print()
        elif num2==1:
            assign6_functions.number_1(width)
            print()
        elif num2==2:
            assign6_functions.number_2(width)
            print()         
        elif num2==3:
            assign6_functions.number_3(width)
            print()
        elif num2==4:
            assign6_functions.number_4(width)
            print()
        elif num2==5:
            assign6_functions.number_5(width)
            print()
        elif num2==6:
            assign6_functions.number_6(width)
            print()
        elif num2==7:
            assign6_functions.number_7(width)
            print()
        elif num2==8:
            assign6_functions.number_8(width)
            print()
        else:
            assign6_functions.number_9(width)
            print()

        print()
        #prompt the user for an answer
        answer=int(input("= "))
        final_answer=assign6_functions.check_answer(num1,num2,answer,operator)
        #tell the user whether their answer is correct or not
        if final_answer=="True":
            print("Correct!")
            print()
            correct+=1
            if operator=="+":
                correct_add+=1
            elif operator=="-":
                correct_sub+=1
            elif operator=="*":
                correct_mul+=1
            else:
                correct_div+=1
        else:
            print("Sorry, that's not correct.")
            print()

#if the user selected yes for mode, show how many of each type of problem
#were presented, and how many of their answers were correct 
if mode=="yes":
    print()
    print("Thanks for playing!")
    print()
    #present total number of addition problems and how many were correct
    if add==0:
        print("No addition problems presented")
    else:
        print("Total addition problems presented:",add)
        if add_attempts==0:
            print("# of extra attempts needed:",add_attempts,"(perfect!)")
        else:
            print("# of extra attempts needed:",add_attempts)
    print()
    #present total number of subtraction problems and how many were correct
    if sub==0:
        print("No subtraction problems were presented")
    else:
        print("Total subtraction problems presented:",sub)
        if sub_attempts==0:
            print("# of extra attempts needed:",sub_attempts,"(perfect!)")
        else:
            print("# of extra attempts needed:",sub_attempts)
    print()
    #present total number of multiplication problems and how many were correct
    if mul==0:
        print("No multiplication problems presented")
    else:
        print("Total multiplication problems presented:",mul)
        if mul_attempts==0:
            print("# of extra attempts needed:",mul_attempts,"(perfect!)")
        else:
            print("# of extra attempts needed:",mul_attempts)
    print()
    #present total number of division problems and how many were correct
    if division==0:
        print("No division problems presented")
    else:
        print("Total division problems presented:",division)
        if div_attempts==0:
            print("# of extra attempts needed:",div_attempts,"(perfect!)")
        else:
            print("# of extra attempts needed:",div_attempts)
#if the user typed in 'no' for the mode, present how many questions the user got
#correct, how many of each type of problem were presented, and how many questions
#the user got with respect to the problem type
else:
    #print how many questions the user got right
    print("You got",correct,"out of",problem_num,"correct!")
    print()
    #present total number of addition problems and how many were correct
    if total_add==0:
        print("No addition problems presented")
    else:
        print("Total addition problems presented:",total_add)
        fraction_add=(correct_add/total_add)*100
        percent_add=format(fraction_add,".1f")
        print("Correct addition problems:",correct_add,"(",percent_add,"%)",sep="")
    print()
    #present total number of subtraction problems and how many were correct
    if total_sub==0:
        print("No subtraction problems presented")
    else:
        print("Total subtraction problems presented:",total_sub)
        fraction_sub=(correct_sub/total_sub)*100
        percent_sub=format(fraction_sub,".1f")
        print("Correct subtraction problems:",correct_sub,"(",percent_sub,"%)",sep="")
    print()
    #present total number of multiplication problems and how many were correct
    if total_mul==0:
        print("No multiplication problems presented")
    else:
        print("Total multiplication problems presented:",total_mul)
        fraction_mul=(correct_mul/total_mul)*100
        percent_mul=format(fraction_mul,".1f")
        print("Correct multiplication problems:",correct_mul,"(",percent_mul,"%)",sep="")
    print()
    #present total number of division problems and how many were correct
    if total_div==0:
        print("No division problems presented")
    else:
        print("Total division problems presented:",total_div)
        fraction_div=(correct_div/total_div)*100
        percent_div=format(fraction_div,".1f")
        print("Correct division problems:",correct_div,"(",percent_div,"%)",sep="")
          






