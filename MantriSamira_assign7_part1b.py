#Samira Mantri 4/4/16 section-3 MantriSamira_assign7_part1b.py

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
                                                                print()
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
                



#Create a loop to ennsure the user enters a correct password
while True:
    password=input("Please enter a password: ")
    if len(password)>=8:
        if username in password:
            print("You cannot use your username as part of your password")
            print()
        else:
            #ensure there is at least one digit
            digit=0
            for w in password:
                if w.isdigit()==True:
                    digit+=1
            if digit>0:
                #ensure there is an uppercase character
                upper_num=0
                for x in password:
                    if x.isupper()==True:
                        upper_num+=1
                if upper_num>0:
                    #ensure there is a lowercase character
                    lower_num=0
                    for y in password:
                        if y.islower()==True:
                            lower_num+=1
                    if lower_num>0:
                        #ensure there are no special characters that are not allowed
                        special_char_tracker=0
                        for z in password:
                            #use ascii conversion to determine whether the character is within the range of the special characters that can be used
                            ascii_conversion=ord(z)
                            if ascii_conversion>=0 and ascii_conversion<=34:
                                special_char_tracker+=1
                            elif ascii_conversion>=39 and ascii_conversion<=47:
                                special_char_tracker+=1
                            elif ascii_conversion>=58 and ascii_conversion<=64:
                                special_char_tracker+=1
                            elif ascii_conversion>=91 and ascii_conversion<=96:
                                special_char_tracker+=1
                            elif ascii_conversion>=123 and ascii_conversion<=127:
                                special_char_tracker+=1
                        if special_char_tracker>0:
                            print("Your password contains at least one invalid character.")
                            print()
                        else:
                            #make sure authorized special characters are in password
                            if "#" in password or "$" in password or "%" in password or "&" in password:
                                print("Your password is valid!")
                                break
                            else:
                                print("Your password must contain at least one 'special' character.")
                                print()
                    else:
                        print("Your password must contain at least one lowercase character.")
                        print()
                else:
                    print("Your password must contain at least one uppercase character.")
                    print()
            else:
                print("Your password must contain at least one digit.")
                print()
                
                                                        
    else:
        print("Passwords must be at least 8 characters long")
        print()



    
