#Samira Mantri 2/6/16 Section 3 MantriSamira_assign2_problem4.py

#Create an input asking the user to enter their file size in kilobytes (KB)
file_sizeKB=(input("Enter a file size, in kilobytes (KB): "))
#A syntax error would have occured if I had mistmatched delimiters
#For example: file_sizeKB=input("Enter a file size, in kilobytes (KB): ')
float_file_sizeKB=float(file_sizeKB)

#Print the file size
print()
print(file_sizeKB,"KB","...")
print()

#Convert the supplied units into bits, bytes, megabytes and gigabytes.
KB_to_bits=float_file_sizeKB*1024*8
KB_to_bytes=float_file_sizeKB*1024
KB_to_megabytes=float_file_sizeKB/1024
#A run-time error would have occured if I typed :KB_to_megabytes=float_file_sizeKB/"1024"
#The reason this would happen is because the delimiters around 1024 would cause the program to think it is a string
#The program would therefore crash because you cannot divide a float by a string
KB_gigabytes=float_file_sizeKB/1024/1024

#format conversion results so that they have commas and two decimal places.
#Also ensure that they line up when printed
format_bits=format(KB_to_bits,">27,.2f")
#I would have encountered a run-time error if I typed: format_bits=format(KB_to_bits,">27,.2s")
#because what I am formatting is not a string, it's a float
format_bytes=format(KB_to_bytes,">26,.2f")
format_megabytes=format(KB_to_megabytes,">22,.2f")
format_gigabytes=format(KB_gigabytes,">22,.2f")
#Another possible syntax error would occur if I typed this instead: format_gigabytes=format(KB_gigabytes">22,.2f")
#The error would occur because there is no comma after KB_gigabytes.

#Print results
print("... in bits",format_bits,"bits")
#A logical error might be if I accidently printed ("... in bits","format_bits","bits")
#Though the program would run, the delimiters around "format_bits" would cause the program to think it is a string
#Therefore, "format_bits" would be printed instead of the variable it represents:format(KB_to_bits,">27,.2f")
print("... in bytes",format_bytes,"bytes")
print("... in megabytes",format_megabytes,"MB")
print("... in gigabytes",format_gigabytes,"GB")




