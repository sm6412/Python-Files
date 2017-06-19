#Samira Mantri 3/10/2016 section-3 MantriSamira_assign5_part3c.py

while True:
    start_num=int(input("Start number: "))
    end_num=int(input("End number: "))
    if start_num>0 and end_num>0:
        if end_num<=start_num:
            print("End number must be greater than start number")
            print()
        else:
            break
    else:
        print("Start and end must be positive")
        print()

print()
spaces=1
for x in range(start_num,end_num+1):
        #check whether each individual number is prime
        for y in range(2,x+1):
            #check to see if number is prime based on whether it equals y
            if x==y:
                if spaces%10==0:
                    print(format(x,">3"),"\n")
                    spaces+=1
                    
                else:
                    print(format(x,">3"),end=" ")
                    spaces+=1
                
            #if the number is not prime there will be no remainders
            elif x%y==0:
                break
            
