#Samira Mantri section-3 5/2/16 MantriSamira_assign10.py

#import the random module
import random

#open file
file_object=open('python_asg10_Roget_Thesaurus.txt','r')
#read the file
alldata=file_object.read()
#close the file
file_object.close()

#split the file by line
split_file=alldata.split("\n")

#create dictionary
dictionary={}

#create a word counter
word_counter=0

#pull apart the lines
for x in range(len(split_file)):
    #split the file by line
    line=split_file[x]
    #split apart the line
    split_line=line.split(",")
    #make the term equal to the first
    term=split_line[0]
    #add 1 to the word counter
    word_counter+=1
    #create a list for the values
    value_list=[]
    for y in range(1,len(split_line)):
        value_list+=[split_line[y]]

    dictionary[term]=value_list


#print how many words are in the thesaurus
print("Total words in thesaurus:",(word_counter-1))
print()

#open song file
song_file=open('bieber_baby.txt','r')
#read file
song_data=song_file.read()
#close file
song_file.close()

#make the text that must be changed the song data
text=song_data

#ask the user to enter a chance value
while True:
    chance=float(input("Enter a % chance to change a word: "))
    if chance>0:
        break
    else:
        print("Invalid input, please try again")


#only keep numbers, alpha, and space
newtext=""
for c in text:
    if c.isalpha() or c.isdigit() or c.isspace():
        #keep it
        newtext+=c

#split words based on whether there is a space
splitwords=newtext.split(" ")

#examine each word in the split up list
for word in splitwords:
    if word=="the":
        print(word,end=" ")
    elif word in dictionary:
        #make sure the chance effects whether or not the word will
        #be converted into one of its synonyms
        if random.random()<chance:
            #pick a random number that represents one of
            #the possible synonyms of this word
            location=random.randint(0,len(dictionary[word])-1)
            #use the synonym
            print(dictionary[word][location].upper(),end=" ")
        else:
            print(word,end=" ")

    #if not, use original word
    else:
        print(word,end=" ")



