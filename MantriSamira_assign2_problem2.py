#Samira Mantri 2/3/16 section:3 MantriSamira_assign2_problem2.py

#Print an opening statement
print("This program will project how much you can earn by investing money in a high-yield account over a 3 month period.")
print()

#create an input asking for the initial investment and the projected annual interest rate
initial_investment=float(input("To begin, enter how much money you would like to initially invest (i.e. 500): "))
interest_rate=float(input("Next, enter your projected annual interest rate. For example, enter 0.05 for 5%: "))
print()

#print "calculating"
print("------- Calculating -------")
print()

#Calculate the starting balance, interest, and ending balance for all three months.
#Make sure to designate them as variables
#month 1
starting_balance1=initial_investment
format_starting_balance1=format(starting_balance1,">20,.2f")
interest1=starting_balance1*(interest_rate/12)
format_interest1=format(interest1,">21,.2f")
ending_balance1=starting_balance1+interest1
format_ending_balance1=format(ending_balance1,">22,.2f")
#month 2
starting_balance2=ending_balance1
format_starting_balance2=format(starting_balance2,">20,.2f")
interest2=starting_balance2*(interest_rate/12)
format_interest2=format(interest2,">21,.2f")
ending_balance2=starting_balance2+interest2
format_ending_balance2=format(ending_balance2,">22,.2f")
#month 3
starting_balance3=ending_balance2
format_starting_balance3=format(starting_balance3,">20,.2f")
interest3=starting_balance3*(interest_rate/12)
format_interest3=format(interest3,">21,.2f")
ending_balance3=starting_balance3+interest3
format_ending_balance3=format(ending_balance3,">22,.2f")

#format headers
interest_header="Interest"
format_interest_header=format(interest_header,">21s")
ending_balance="Ending Balance"
format_ending_header=format(ending_balance,">22s")

#print results
print("Month Starting Balance",format_interest_header,format_ending_header)
print("1",format_starting_balance1,format_interest1,format_ending_balance1)
print("2",format_starting_balance2,format_interest2,format_ending_balance2)
print("3",format_starting_balance3,format_interest3,format_ending_balance3)
