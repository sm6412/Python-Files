#Samira Mantri 4/4/16 section-3 MantriSamira_assign7_part2b.py

#Ask the user for their name
name=input("Name: ")

#Create a new, cleaned up word without non-letters
new_word=""
for x in name:
    ascii_value=ord(x)
    if ascii_value>=65 and ascii_value<=90:
        new_word+=x
    elif ascii_value>=97 and ascii_value<=122:
        new_word+=x

#ensure that every letter in the word is in lowercase    
cleaned_name=new_word.lower()

#display cleaned up word
print("Your 'cleaned up' name is:",cleaned_name)
print("Your 'cleaned up' name reduces to:")

#create an accumulator to build the addition string
added_num=""
#create an accumulator to measure the placement and determine which
#aspect of the string needs to be presented
placement=0
#create a accumulator to add the values of each letter
total=0
for y in cleaned_name:
    if y=="a":
        placement+=1
        total+=1
        if (len(cleaned_name)-1)>=placement:
            added_num+="1 + "
        else:
            added_num+="1"
    if y=="b":
         placement+=1
         total+=2
         if (len(cleaned_name)-1)>=placement:
             added_num+="2 + "
         else:
             added_num+="2"
    if y=="c":
        placement+=1
        total+=3
        if (len(cleaned_name)-1)>=placement:
            added_num+="3 + "
        else:
            added_num+="3"
    if y=="d":
        placement+=1
        total+=4
        if (len(cleaned_name)-1)>=placement:
            added_num+="4 + "
        else:
            added_num+="4"
    if y=="e":
        placement+=1
        total+=5
        if (len(cleaned_name)-1)>=placement:
            added_num+="5 + "
        else:
            added_num+="5"
    if y=="f":
        placement+=1
        total+=6
        if (len(cleaned_name)-1)>=placement:
            added_num+="6 + "
        else:
            added_num+="6"
    if y=="g":
        placement+=1
        total+=7
        if (len(cleaned_name)-1)>=placement:
            added_num+="7 + "
        else:
            added_num+="7"
    if y=="h":
        placement+=1
        total+=8
        if (len(cleaned_name)-1)>=placement:
            added_num+="8 + "
        else:
            added_num+="8"
    if y=="i":
        placement+=1
        total+=9
        if (len(cleaned_name)-1)>=placement:
            added_num+="9 + "
        else:
            added_num+="9"
    if y=="j":
        placement+=1
        total+=10
        if (len(cleaned_name)-1)>=placement:
            added_num+="10 + "
        else:
            added_num+="10"
    if y=="k":
        placement+=1
        total+=11
        if (len(cleaned_name)-1)>=placement:
            added_num+="11 + "
        else:
            added_num+="11"
    if y=="l":
        placement+=1
        total+=12
        if (len(cleaned_name)-1)>=placement:
            added_num+="12 + "
        else:
            added_num+="12"
    if y=="m":
        placement+=1
        total+=13
        if (len(cleaned_name)-1)>=placement:
            added_num+="13 + "
        else:
            added_num+="13"
    if y=="n":
        placement+=1
        total+=14
        if (len(cleaned_name)-1)>=placement:
            added_num+="14 + "
        else:
            added_num+="14"
    if y=="o":
        placement+=1
        total+=15
        if (len(cleaned_name)-1)>=placement:
            added_num+="15 + "
        else:
            added_num+="15"
    if y=="p":
        placement+=1
        total+=16
        if (len(cleaned_name)-1)>=placement:
            added_num+="16 + "
        else:
            added_num+="16"
    if y=="q":
        placement+=1
        total+=17
        if (len(cleaned_name)-1)>=placement:
            added_num+="17 + "
        else:
            added_num+="17"
    if y=="r":
        placement+=1
        total+=18
        if (len(cleaned_name)-1)>=placement:
            added_num+="18 + "
        else:
            added_num+="18"
    if y=="s":
        placement+=1
        total+=19
        if (len(cleaned_name)-1)>=placement:
            added_num+="19 + "
        else:
            added_num+="19"
    if y=="t":
        placement+=1
        total+=20
        if (len(cleaned_name)-1)>=placement:
            added_num+="20 + "
        else:
            added_num+="20"
    if y=="u":
        placement+=1
        total+=21
        if (len(cleaned_name)-1)>=placement:
            added_num+="21 + "
        else:
            added_num+="21"
    if y=="v":
        placement+=1
        total+=22
        if (len(cleaned_name)-1)>=placement:
            added_num+="22 + "
        else:
            added_num+="22"
    if y=="w":
        placement+=1
        total+=23
        if (len(cleaned_name)-1)>=placement:
            added_num+="23 + "
        else:
            added_num+="23"
    if y=="x":
        placement+=1
        total+=24
        if (len(cleaned_name)-1)>=placement:
            added_num+="24 + "
        else:
            added_num+="24"
    if y=="y":
        placement+=1
        total+=25
        if (len(cleaned_name)-1)>=placement:
            added_num+="25 + "
        else:
            added_num+="25"
    if y=="z":
        placement+=1
        total+=26
        if (len(cleaned_name)-1)>=placement:
            added_num+="26 + "
        else:
            added_num+="26"

#format the string to include the '=' sign
format_addition_string=(str(added_num))+" = "+(str(total))
#print the addition string with the correct format and information
print(format_addition_string)


#make sure to reduce the number if it is larger than 9
if total>9:
    while True:
        added_int=0
        for x in str(total):
            added_int+=int(x)
        if added_int>9:
            #print the reduction
            print("Further reduction:",added_int)
            total=str(added_int)
        else:
            final_total=added_int
            #print the reduction
            print("Further reduction:",added_int)
            break
else:
    final_total=total

#print the meaning of the total
if final_total==0:
    print("This name means ...Emptiness")
elif final_total==1:
    print("This name means ...Independence")
elif final_total==2:
    print("This name means ...Quiet")
elif final_total==3:
    print("This name means ...Charming")
elif final_total==4:
    print("This name means ...Harmony")
elif final_total==5:
    print("This name means ...New Directions")
elif final_total==6:
    print("This name means ...Love")
elif final_total==7:
    print("This name means ...Spirituality")
elif final_total==8:
    print("This name means ...Organization")
else:
    print("This name means ...Romantic")
            

        
            

           
      
