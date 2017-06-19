#Samira Mantri 3/9/16 section-3 MantriSamira_assign5_part2.py


while True:
    #ask the user for the number of students in the class
    students=int(input("How many students are in your class? "))
    #make sure the user entered a valid number, if not, prompt them again
    if students>0:
        break
    else:
        print("Invalid # of students, try again.")
        print()

while True:
    #ask the user how many tests are in the class
    tests=int(input("How many tests in this class? "))
    #make sure the user entered a valid number, if not, prompt them again
    if tests>0:
        print()
        print("Here we go!")
        print()
        break
    else:
        print("Invalid # of tests, try again.")

#set avg equal to zero
total_avg=0
for x in range(1,students+1):
    print("****","Student #",x,"****",sep="")
    #set individual score equal to zero
    #this accumlutor will keep track of scores for one individual 
    individual_score=0
    for y in range(1,tests+1):
        while y<=tests:
            #ask user for the score of their test
            formatted_test_num="#"+str(y)+": "
            print("Enter score for test",formatted_test_num,end="")
            score=int(input())
            #Make sure the score is valid
            if score>=0:
                individual_score+=score
                break
            else:
                print("Invalid score, try again")
    #calculate individual avg
    avg=individual_score/tests
    #add individual avgs together 
    total_avg+=avg
    #print the individual avg 
    formatted_student_num="#"+str(x)
    print("Average score for student",formatted_student_num,"is",format(avg,".2f"))
    print()
#once each student has his/her scores and avg presented, print the class avg
print("Average score for all students is:",format(total_avg/students,".2f"))           
                
