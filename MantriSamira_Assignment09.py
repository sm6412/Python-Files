#Samira Mantri 4/26/16 section-3 MantriSamira_Assignment09.py

#check to see whether the program can wrong without an error
try:
    #ask user for a class to grade
    filename=input("Enter a class to grade (i.e. class1 for class1.txt): ")
    #open the file
    file_object= open(filename+".txt","r")

except:
    #tell user the file cannot be found if it does not exist
    print("File cannot be found")

else:
    #if program does not crash tell the user the file was opened
    print("Successfully opened")
    print()
    print("**** ANALYZING ****")
    print()
    #seperate the information by lines into a list
    file=file_object.read()
    new_file=file.split("\n")

    #use accumulators to count correct and incorrect lines 
    correct_lines=0
    incorrect_lines=0
    
    #create answer key
    answerkey = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
    list_answerkey=answerkey.split(",")

    #create two score lists, one to sort one not to
    score=[]
    score2=[]

    #create a nyu id list
    id_list=[]

    for y in range(len(new_file)):
        single_list=new_file[y]
        #seperate list by commas
        new_list=str(single_list)
        final_list=new_list.split(",")
        #create an accumulator to keep track of score
        points=0
        #create an answer list
        answer_list=[]
        for b in range(1,len(final_list)):
            answer_list+=[final_list[b]]

        counter=0
        #count whether there are 26 characters in the line
        for c in range(len(final_list)):
            counter+=1
        if counter==26:
            #compare answer list to answer key
            for a in range(len(answer_list)):
                #if answer is correct add 4 points
                if answer_list[a]==list_answerkey[a]:
                    points+=4
                #if there is no answer no points are earned
                elif answer_list[a]=="":
                    points+=0
                #if answer is wrong take away 1 point
                else:
                    points-=1
            #make sure id is 9 characters long
            if len(final_list[0])!=9:
                print("Invalid line of data: N# is invalid a")
                print(single_list)
                print()
                incorrect_lines+=1
            else:
                nyu_id=final_list[0]
                #make sure first character of nyu id is N
                if nyu_id[0]!="N":
                    print("Invalid line of data: N# is invalid b")
                    print(single_list)
                    print()
                    incorrect_lines+=1
                else:
                    numeric_lines=0
                    for x in range(1,len(nyu_id)):
                        #count to see whether remaining characters are numbers
                        if (nyu_id[x]).isnumeric()==True:
                                numeric_lines+=1
                    #if the nyu id is the right lenght increase the num
                    #of valid lines and add the score for that student
                    #to the score list
                    if numeric_lines==8:
                        id_list+=[nyu_id]
                        correct_lines+=1
                        score+=[points]
                        score2+=[points]

                    else:
                        #if the nyu id is not valid tell the user
                        print("Invalid line of data: N# is invalid c")
                        print(single_list)
                        print()
                        incorrect_lines+=1
                        
                     
                    
        else:
            incorrect_lines+=1
            #tell the user if there is not 26 lines
            print("Invalid line of data: does not contain exactly 26 values:")
            print(single_list)
            print()

     
        
                

    if incorrect_lines==0:
        #if there are no errors print a statement expressing this
        print("No errors found!")
        print()
        
    print("**** REPORT ****")
    print()
    #print number of valid lines
    print("Total valid lines of data:",correct_lines)
    #print number of invalid lines
    print("Total invalid lines of data:",incorrect_lines)
    print()
    #calculate average
    average=(sum(score)/len(score))
    format_average=format(average,".2f")
    #print the average
    print("Mean (average) score:",format_average)
    #print highest score
    print("Highest score:",max(score))
    #print lowest score
    print("Lowest score:",min(score))
    #print range of scores
    print("Range of scores:",(max(score)-min(score)))

    #sort score list
    score.sort()
    #determine the median num
    if len(score)%2==0:
        median_value=int(len(score)/2)
        med1=score[median_value]
        med2=score[median_value-1]
        median=((med1+med2)/2)
        print("Median score:",format(median,".1f"))
    else:
        #if odd take middle num of score list
        middle_num=((len(score))-1)/2
        int_num=int(middle_num)
        print("Median score:",score[int_num])

    #create a unique list to keep track of different grades
    unique=[]
    #create seen list to keep track of the number of times the same grade
    #is observed
    seen=[]
    for x in score:
        #add grade to unique list if it is not already in it
        if x not in unique:
            unique+=[x]
            #add a corresponding spot on the seen list
            seen.append(0)

        else:
            #if grade comes up again increase its number on the seen list
            location=unique.index(x)
            seen[location]+=1

    #find greatest number in seen list
    max_num=max(seen)
    max_string=""
    num_counter=0
    #check to see whether other grades are just as common
    for b in range(len(seen)):
        if seen[b]==max_num:
            if num_counter==0:
                max_string+=(str(unique[b]))
            else:
                max_string+=(" "+str(unique[b]))
            num_counter+=1
            
    #print the mode score
    print("Mode score(s):",max_string)

    #ask the user if they want to curve the grade
    while True:
        grade_type=input("Would you like to apply a curve to the score? (y)es or (n)o? ")
        if grade_type=="y" or grade_type=="n":
            break
        else:
            print("Invalid answer, please try again.")

    if grade_type=="n":
        #create the name of the grade file
        grade_filename=filename+"_grades.txt"

        #open the file so information can be written into it
        open_file=open(grade_filename,'w')

        #write the nyu id and grade into the file
        for q in range(len(id_list)):
                open_file.write((str(id_list[q])+","+str(score2[q]))+"\n")
            
        #close the file
        open_file.close()

        #print a conclusion string
        print("A grade file has been written",("("+grade_filename+")"))
    else:
        while True:
            #ask the user for the mean score
            new_mean=int(input("Enter desired mean score: "))
            if new_mean>0:
                break
            else:
                print("Invalid choice, please try again")

        #create the name of the grade file
        grade_filename=filename+"_grades_with_curve.txt"

        #open the file so information can be written into it
        open_file=open(grade_filename,'w')   

        if new_mean<float(format_average):
            #calculate points taken away from grade
            curve_points=float(format_average)-new_mean
        else:
            #calculate points added to grade
            curve_points=new_mean-float(format_average)
            

        #write the nyu id and grade into the file
        for q in range(len(id_list)):
            #if the mean is less than the average curve down
            if new_mean<float(format_average):
                new_grade=score2[q]-curve_points
            else:
                #if the mean is more than the average curve up
                new_grade=score2[q]+curve_points
            format_new_grade=format(new_grade,".2f")

            #write the nyu id, grade, and curved grade into the file
            open_file.write((str(id_list[q])+","+str(score2[q]))+","+str(format_new_grade)+"\n")
        
            
        #close file
        open_file.close()

        #print a conclusion string
        print("Done! A new grade file has been written",("("+grade_filename+")"))

            
            


    



