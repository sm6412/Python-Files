#Samira Mantri 3/10/16 section-3 MantriSamira_assign5_part3b.py

#print that 1 is not a prime number
print("1 is technically not a prime number.")

#establish a loop to determine prime numbers
#set range from 1 to 1000
for x in range(1,1001):
        #check whether each individual number is prime
        for y in range(2,x+1):
            #check to see if number is prime based on whether it equals y
            if x==y:
                print(x,"is a prime number!")
            #if the number is not prime there will be no remainders
            elif x%y==0:
                break
            
           
     
