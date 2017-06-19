#Samira Mantri 4/13/16 section-3 MantriSamira_assign8_part1.py

while True:
    #ask the user to enter a num greater than 10
    n=int(input("Please enter a positive integer that is greater than or equal to 10: "))
    #make sure the entered number is valid
    if n<10:
        print("Invalid, please try again")
        print()
    else:
        print()
        break

#create list
P_list=[]
for i in range(n+1):
    P_list+=["P"]

#use comparison list to edit P_list
comparison_list=[]
for num in range(len(P_list)):
    comparison_list+=[num]

#make sure that 0 and 1 are listed as not prime
if P_list.index("P")==0 or P_list.index("P")==1:
    P_list[0]="N"
    P_list[1]="N"


#establish a loop to check for prime numbers
for x in range(2,len(P_list)):
    for y in range(2,len(P_list)):
        #if the number does not equal "P" skip
        if P_list[y]=="P":
            #make sure the number is not the same as the testing one
            if int(comparison_list[x])!=y:
                #ensure whether the number goes evenly into the list number
                if y%comparison_list[x]==0:
                    #if the number is not prime change "P" to
                    P_list[y]="N"
    


p_counter=0
#print all prime numbers
for z in range(len(P_list)):
    if P_list[z]=="P":
        p_counter+=1
        
#create counter to keep track of how many numbers are on each line
counter=1
for p in range(2,len(P_list)):
    if P_list[p]=="P":
        #if 10 does not go into counter then keep adding numbers to same line
        if counter%10==0:
            print(format(p,"<5"),"\n")
            counter+=1
        else:
            print(format(p,"<5"),end=" ")
            counter+=1

        
           


 

       
        
        

        


        
