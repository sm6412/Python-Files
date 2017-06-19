#Samira Mantri section-3 3/30/16 MantriSamira_assign7_part1a.py

#Part 1a

#create a loop to ensure the user enters a correct username
while True:
        #ask the user for a username
        username=input("Please enter a username: ")
        #make sure only the correct number of characters are in the username
        if len(username)>=8 and len(username)<=15:
                #make sure the username only contains alphanumeric characters
                if username.isalnum()==True:
                        if username[0]=="1" or username[0]=="2" or username[0]=="3" or username[0]=="4" or username[0]=="5" or username[0]=="6" or username[0]=="7" or username[0]=="8" or username[0]=="9":
                                print("The first/last character in your username cannot be a digit")
                                print()
                        else:
                                #ensure the first and last character of the username are not digits
                                if username[-1]=="1" or username[-1]=="2" or username[-1]=="3" or username[-1]=="4" or username[-1]=="5" or username[-1]=="6" or username[-1]=="7" or username[-1]=="8" or username[-1]=="9":
                                        print("The first/last character in your username cannot be a digit")
                                        print()
                                else:
                                        #ensure the username contains at least one digit
                                        digits=0
                                        for z in username:
                                                if z.isdigit()==True:
                                                        digits+=1
                                        if digits>0:
                                                #ensure there is at least one uppercase character
                                                upper_num=0
                                                for x in username:
                                                        if x.isupper()==True:
                                                                upper_num+=1
                                                if upper_num>0:
                                                        #ensure there is at least one lowercase character
                                                        lower_num=0
                                                        for y in username:
                                                                if y.islower()==True:
                                                                        lower_num+=1
                                                        if lower_num>0:
                                                                #if all conditions are met break loop
                                                                print("Your username is valid!")
                                                                break

                                                        else:
                                                                print("Your username must contain at least one lowercase character.")
                                                                print()   
                                

                                                else:
                                                        print("Your username must contain at least one uppercase character.")
                                                        print()
                                        else:
                                                print("Username must contain at least one digit.")
                                                print()
                                        
        
                else:
                     print("Username must only contain alphanumeric characters.")
                     print()
        else:
                print("Username must be between 8 and 15 characters.")
                print()


               



        









    
    
            
        
    





