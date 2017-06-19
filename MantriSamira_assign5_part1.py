#Samira Mantri 3/9/16 section-3 MantriSamira_assign5_part1.py

while True:
    #Ask the user how many bottles are on the wall
    bottles=int(input("How many bottles of beer on the wall? "))
    #Make sure the number of bottles on the wall are valid
    if bottles>0:
        print()
        print("OK, here we go!")
        print()
        break
    else:
        print("Sorry, that's not a valid number of bottles. Try again.")
        print()
        
#create the song
bottles_left=bottles              
for x in range(bottles,0,-1):
    #make sure to keep track of the new number of bottles
    new_bottles=x-1
    #if there is only one bottle left make sure to adjust the sentence
    if x==1:
        print(x,"bottle of beer on the wall,",x,"bottle of beer.")
        #if there are zero bottles left, the closing statement should be different
        print("Take one down, pass it around, no more bottles of beer on the wall!")
    else:
        print(x,"bottles of beer on the wall,",x,"bottles of beer.")
        if new_bottles==1:
            print("Take one down, pass it around,",new_bottles,"bottle of beer on the wall.")
        else:
            print("Take one down, pass it around,",new_bottles,"bottles of beer on the wall.")
    
    print()
