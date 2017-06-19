#Samira Mantri 2/6/16 Section 3 MantriSamira_assign2_problem3.py

#Create an input asking for the user's name. Store as variable
name=input("What is your name? ")

#Create an input asking for the name of the user's class. Store as variable
name_of_class=input("What class are you in? ")
print()

#Create an input asking the user for the weighting of their tests. Store as variable
test_weight=float(input("How much are tests worth in this class (i.e. 0.40 for 40%): "))

#Ask the user for the 3 test scores. Store as variables
test_score1=float(input("Enter test score #1: "))
test_score2=float(input("Enter test score #2: "))
test_score3=float(input("Enter test score #3: "))
print()

#Calculate the student's test average, then print it out
test_average=(test_score1+test_score2+test_score3)/3
format_test_average=format(test_average,".2f")
print("Your test average is:",format_test_average)
print()

#Create an input asking the user for the weighting of their homework assignments. Store as variable.
hw_weight=float(input("How much are homework assignments worth in this class (i.e. 0.60 for 60%): "))

#Create an input asking for the user's 3 hw assignment scores. Store as variables.
hw1=float(input("Enter homework score #1: "))
hw2=float(input("Enter homework score #2: "))
hw3=float(input("Enter homework score #3: "))
print()

#Calculate the student's hw average, then print it out
hw_average=(hw1+hw2+hw3)/3
format_hw_average=format(hw_average,".2f")
print("Your homework average is:",format_hw_average)
print()

#Calculate the student's final grade the print it out
final_grade=(test_average*test_weight)+(hw_average*hw_weight)
format_final_grade=format(final_grade,".2f")
format_name=name+"."
print("Thanks,",format_name,"Your final score in", name_of_class,"is",format_final_grade)


