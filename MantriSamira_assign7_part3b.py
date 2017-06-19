#Samira Mantri 4/7/16 section-3 MantriSamira_assign7_part3b.py

import random

# function:   add_letters
# input:      a word to scramble (String) and a number of letters (integer)
# processing: adds a number of random letters (A-Z; a-z) after each letter 
#             in the supplied word. for example, if word="cat" and num=1 
#             we could generate any of the following:
#             cZaQtR
#             cwaRts
#             cEaett
# 
#             if word="cat" and num=2 we could generate any of the following:
#             cRtaHFtui
#             cnnaNYtjn
#             czAaAitym
#
# output:     returns the newly generated word
def add_letters(word, num):
    final_word=""
    for x in word:
        new_word=""
        for y in range(num):
            chooser=random.randint(1,2)
            if chooser==1:
                new_char=chr(random.randint(65,90))
            else:
                new_char=chr(random.randint(97,122))
            new_word+=new_char
        final_word+=(x+new_word)
    return final_word
  

# function:   remove_letters
# input:      a word to unscramble (String) and the number of characters to remove (integer)
# processing: the function starts at the first position in the supplied word and keeps it.
#             it then removes "num" characters from the word. the process is repeated again
#             if the word contains additional characters - the next character is kept
#             and "num" more characters are removed.  For example, if word="cZaYtU" and
#             num=1 the function will generate the following:
#        
#             cat (keeping character 0, removing character 1, keeping character 2, removing
#                  character 3, keeping character 4, removing character 5)
#
# output:     returns the newly unscrambed word

def remove_letters(word, num):
    cleaned_word=""
    for y in range(0,len(word),num+1):
        if y<len(word):
            added_char=word[y]
            cleaned_word+=added_char
        else:
            added_char=word[y-1]
            cleaned_word+=added_char
    return cleaned_word
        

# function:   shift_characters
# input:      a word (String) and a number of characters to shift (integer)
# processing: shifts each character in the supplied word to another position in the ASCII
#             table. the new position is dictated by the supplied integer.  for example,
#             if word = "apple" and num=1 the newly generated word would be:
#
#             bqqmf
#
#             because we added +1 to each character. if we were to call the function with
#             word = "bqqmf" and num=-1 the newly generated word would be:
#           
#             apple
#
#             because we added -1 to each character, which shifted each character down by
#             one position on the ASCII table.
#
# output:     returns the newly generated word
def shift_characters(word, num):
    new_word=""
    new_value=0
    for x in word:
        ascii_value=ord(x)
        new_value=(ascii_value+num)
        new_char=chr(new_value)
        new_word+=new_char
    return new_word



#Part 3b

#create a loop to keep allowing the user to encode and decode strings
while True:
    #create a loop to ensure the user enters a valid string
    while True:
        #ask the user whether they want to encode or decode a string, or quit
        function=input("(e)ncode, (d)ecode, or (q)uit: ")
        if function=="e" or function=="d" or function=="q":
            break
        else:
            print("Invalid, please try again")
    if function=="q":
        break
    #create a loop to ensure the entered number is within the correct range
    while True:
        #ask the user to enter a number between 1 and 5
        num=int(input("Enter a number between 1 and 5: "))
        if num>=1 and num<=5:
            break
        else:
            print("Invalid, please try again")
    #encode the string if 'e' is entered
    if function=="e":
        word=input("Enter a phrase to encode: ")
        #add letters to the string
        encoded_word=add_letters(word,num)
        #shift the string
        print("Your encoded word is:",shift_characters(encoded_word,num))
        print()
    #decode the string if 'd' is entered
    else:
        word=input("Enter a phrase to decode: ")
        #shift the string
        decoded_word=shift_characters(word,-num)
        #remove letters from the string
        print("Your decoded word is:",remove_letters(decoded_word,num))
        print()
       
              
        
        
        












                
        
