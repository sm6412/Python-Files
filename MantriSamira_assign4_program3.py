#Samira Mantri 2/27/16 section:3 MantriSamira_assign4_program3.py


while True:
    #ask the user how many columns they want
    columns=int(input(" How many columns? "))
    #make sure there are more than zero columns
    if columns>0:
        #ask user for the direction of the arrow
        direction=(input(" Direction? (l)eft or (r)ight: "))
        #adjust the arrow so it can face right
        if direction=="r":
            # set arrowhead equal to one
            arrowhead=1
            #modify the top half or the arrow
            while arrowhead<columns:
                print((arrowhead*" ")+"*")
                arrowhead+=1
            #modify the bottom half of the arrow
            while columns>=1:
                print((columns*" ")+"*")
                columns-=1
            break
        #adjust the arrow so it can face left
        elif direction=="l":
            #set arrowhead equal to one
            arrowhead=1
            #create a new variable to keep track of the columns lost during
            #the first part of this loop
            columns2=1
            #modify the top part of the arrow
            while columns>1:
                print((columns*" ")+"*")
                columns-=1
                columns2+=1
            #modify the bottom part of the error
            while arrowhead<=columns2:
                print((arrowhead*" ")+"*")
                arrowhead+=1
            break
        else:
            print(" Invalid entry,try again!")
                    
    else:
        print(" Invalid entry, try again!")




    

 
        
