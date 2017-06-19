#Samira Mantri 2/3/16 section:3 MantriSamira_assign2_problem1.py

#Print a welcome statement
print("Hello! I'm here to help you calculate your tip.")

#Ask how much the bill is in the form of an input
bill_amount=float(input("How much was your bill? (Enter a numeric value without commas or dollar signs): "))

#Ask how much tip to leave in the form of an input
tip_amount=float(input("How much tip would you like to leave? (Enter an integer value): "))
decimal_tip=tip_amount/100

#Ask how many poeple will split the bill in the form of an input
num_of_people=float(input("How many individuals are splitting the bill? (Enter an integer value): "))
print()

#Calculate the tip
final_tip= bill_amount*decimal_tip
format_final_tip=format(final_tip,".2f")
float_format_final_tip=float(format_final_tip)

#Calculate final bill
final_bill=bill_amount+float_format_final_tip

#Calculate how much each person must contribute to the bill
amount_contributed= (final_bill)/num_of_people
format_amount_contributed=format(amount_contributed,".2f")

#Print a statement thanking the user
print("Thanks! Calculating your bill & tip...")
print()

#Print how much you need to leave as tip
string_format_final_tip=str(float_format_final_tip)
money_amount="$"+string_format_final_tip

print("You need to leave", money_amount,"as a tip.")

#Print how much the total bill will be
print("Your total bill will be $",final_bill,".",sep='')

#Print what each individual should pay
print("Each individual should pay $", format_amount_contributed, ".",sep='')
