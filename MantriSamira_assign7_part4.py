#Samira Mantri 4/7/16 section-3 MantriSamira_assign7_part4.py

# function:   string_length
# input:      a word (String)
# processing: computes the length of the supplied String (without using the len() function)
# output:     returns the length of the string (integer)

def string_length(string):
    length=0
    for x in string:
        length+=1
    return length

# function:   string_isalpha
# input:      a word (String)
# processing: determines if the supplied String contains all alphabetic characters (A-Z,a-z)
#             DO NOT USE THE "isalpha()" METHOD!
# output:     returns True of False (boolean)

def string_isalpha(string):
    counter=0
    for x in string:
        ascii_value=ord(x)
        if ascii_value>=0 and ascii_value<=64:
            counter+=1
        elif ascii_value>=91 and ascii_value<=96:
            counter+=1
        elif ascii_value>=123 and ascii_value<=127:
            counter+=1
    if counter>0:
        return False
    else:
        alpha_counter=0
        for x in string:
            ascii_value=ord(x)
            if ascii_value>=65 and ascii_value<=90:
                alpha_counter+=1
            elif ascii_value>=97 and ascii_value<=122:
                alpha_counter+=1
        if alpha_counter>0:
            return True
        else:
            return False


# function:   string_isupper
# input:      a word (String)
# processing: determines if the supplied String contains all uppercase characters (A-Z)
#             DO NOT USE THE "isupper()" METHOD!
# output:     returns True of False (boolean)
def string_isupper(string):
    counter=0
    for x in string:
        ascii_value=ord(x)
        if ascii_value>=0 and ascii_value<=64:
            counter+=1
        elif ascii_value>=91 and ascii_value<=96:
            counter+=1
        elif ascii_value>=123 and ascii_value<=127:
            counter+=1
        elif ascii_value>=97 and ascii_value<=122:
            counter+=1
    if counter>0:
        return False
    else:
        alpha_counter=0
        for x in string:
            ascii_value=ord(x)
            if ascii_value>=65 and ascii_value<=90:
                alpha_counter+=1
        if alpha_counter>0:
            return True
        else:
            return False

# function:   string_isupper
# input:      a word (String)
# processing: determines if the supplied String contains all uppercase characters (A-Z)
#             DO NOT USE THE "isupper()" METHOD!
# output:     returns True of False (boolean)

def string_isdigit(string):
    counter=0
    for x in string:
        ascii_value=ord(x)
        if ascii_value>=0 and ascii_value<=47:
            counter+=1
        elif ascii_value>=58 and ascii_value<=127:
            counter+=1
        
    if counter>0:
        return False
    else:
        digit_counter=0
        for x in string:
            ascii_value=ord(x)
            if ascii_value>=48 and ascii_value<=57:
                digit_counter+=1
        if digit_counter>0:
            return True
        else:
            return False

# function:   string_swapcase
# input:      a word (String)
# processing: swaps uppercase characters with lowercase characters & vice-versa
#             DO NOT USE THE "swapcase()" METHOD!
# output:     returns a new copy of the String
def string_swapcase(string):
    new_string=""
    for x in string:
        ascii_value=ord(x)
        if ascii_value>=97 and ascii_value<=122:
            new_value=ascii_value-32
            for y in range(65,91):
                if new_value==y:
                    final_value=chr(y)
                    new_string+=final_value
        elif ascii_value>=65 and ascii_value<=90:
            new_value=ascii_value+32
            for z in range(97,123):
                if new_value==z:
                    final_value=chr(z)
                    new_string+=final_value
        else:
            new_string+=x
            
                
    return new_string


# function:   string_lower
# input:      a word (String)
# processing: converts all characters in a String to their lowecase equivalents
#             DO NOT USE THE "lower()" METHOD OR "str.lower()"!
# output:     returns a new copy of the String

def string_lower(string):
    new_string=""
    for x in string:
        ascii_value=ord(x)
        if ascii_value>=65 and ascii_value<=90:
            new_value=ascii_value+32
            for z in range(97,123):
                if new_value==z:
                    final_value=chr(z)
                    new_string+=final_value
        else:
            new_string+=x

    return new_string


















    


