#Samira Mantri 3/10/16 section-3 MantriSamira_assign5_part3a.py 


while True:
    #ask the user to enter a positive number
    num=int(input("Enter a positive number to test: "))
    #make sure the number is positive
    if num>0:
        break
    else:
        print("Sorry, that's not a positive number. Try again.")
print()
#if num is 1 it is immediately prime
if num==1:
    print("1 is not a prime number.")
else:
    for x in range(2,num+1):
        #if x is the same as the number it is prime
        if num==x:
            if x!=2:
                print()
                print(num,"is a prime number!")
            else:
                print(num,"is a prime number!")
        else:
            #continue loop if there is no number that goes into the number
            #the user entered 
            if num%x!=0:
                print(x,"is NOT a divisor of",num,"... continuing")
            #if a number goes into the entered one tell the user which one
            #it is before breaking the loop and telling them that their
            #number is not prime
            else:
                #if 2 is immediately a divisor then adjust the statement
                #to make more sense
                if x==2:
                    print(x,"is a divisor of",num)
                else:
                    print(x,"is a divisor of",num,"... stopping")
                print()
                print(num,"is not a prime number.")
                break
        
