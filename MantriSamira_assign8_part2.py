#Samira Mantri section-3 4/23/16 MantriSamira_assign8_part2.py

#Part 2a

#product lists

product_names = ["hamburger", "cheeseburger", "small fries"]
product_costs = [0.99, 1.29, 1.49]
product_amount= [10,5,20]


while True:
    #ask the user if they wish to search for a product, quit, list
    #products, their prices, and quantity, add a product, remove a product
    #give a report or update a product
    answer=input("(s)earch, (l)ist, (a)dd, (r)emove, (u)pdate, r(e)port or (q)uit: ")
    lowercase_answer=answer.lower()
    if lowercase_answer=="s":
        #if the user wishes to search for a product make sure the product
        #is available at the resturant
        product=input("Enter a product name: ")
        lowercase_product=product.lower()
        if lowercase_product in product_names:
            #use the product's location in the list to determine the price
            price_location=product_costs[product_names.index(lowercase_product)]
            format_product='"'+lowercase_product+'"'
            #print the name and price of the product
            print('We sell',format_product,'at',price_location,'per unit')
            #print the amount of that product that is in stock
            print("We currently have",product_amount[product_names.index(lowercase_product)],"in stock")
            print()
        else:
            #if it is not an available product tell the user
            print("Sorry, we don't ", 'sell "',lowercase_product,'"',sep="")
            print()
    elif lowercase_answer=="l":
        #format the headers
        format_placement=format("Product","<26s")
        print(format_placement,end="")
        format_price=format("Price","<7s")
        print(format_price,end="")
        format_quantity=format("Quantity","<s")
        print(format_quantity)
        #create a loop to display the different products with their prices and
        #their quantities
        for x in range(len(product_names)):
            format_placement=format(product_names[x],"<26s")
            print(format_placement,end="")
            format_price=format(product_costs[x],"<7.2f")
            print(format_price,end="")
            format_quantity=product_amount[x]
            print(format_quantity)
        print()
    
    elif lowercase_answer=="a":
        while True:
            #make sure the product is not already available
            new_product=input("Enter a new product name: ")
            if new_product in product_names:
                print("Sorry, we already sell that product. Try again.")
            else:
                product_names+=[new_product]
                break
        while True:
            #make sure the cost is greater than 0
            new_cost=float(input("Enter a product cost: "))
            if new_cost<=0:
                print("Invalid cost. Try again.")
            else:
                format_new_cost=format(new_cost,".2f")
                product_costs+=[float(format_new_cost)]
                break
        while True:
            #make sure the quantity is more than 0
            new_amount=int(input("How many products do we have? "))
            if new_amount<=0:
                print("Invalid quantity. Try again.")
            else:
                product_amount+=[new_amount]
                break
        print("Product added!")
        print()

    elif lowercase_answer=="r":
        #make sure the user enters a valid product to remove
        remove_product=input("Enter a product name: ")
        lower_remove=remove_product.lower()
        if lower_remove in product_names:
            #remove the product, its cost, and quantity
            product_location=product_names.index(lower_remove)
            del product_amount[product_location]
            del product_costs[product_location]
            product_names.remove(lower_remove)
            print("Product removed!")
            print()
        else:
            #if the product does not exist tell the user
            print("Product doesn't exist. Can't remove.")
            print()

    elif lowercase_answer=="u":
        #ask the user to enter a product name
        update=input("Enter a product name: ")
        lower_update=update.lower()
        #make sure the product name is valid
        if lower_update in product_names:
            #ask user what they wish to update
            print("What would you like to update?")
            update_type=input("(n)ame, (c)ost or (q)uantity: ")
            #make sure the update type is valid
            if update_type=="n" or update_type=="c" or update_type=="q":
                if update_type=="n":
                    while True:
                        #ask the user to enter a new name
                        new_name=input("Enter a new name: ")
                        #make sure the name is brand new
                        if new_name in product_names:
                            print("Duplicate name!")
                        else:
                            location=product_names.index(update)
                            product_names[location]=new_name
                            #print new name
                            print("Product name has been updated")
                            print()
                            break

                elif update_type=="c":
                    while True:
                        #ask user for new price
                        new_price=float(input("Enter a new cost: "))
                        #make sure the price is valid
                        if new_price>0:
                            location=product_names.index(update)
                            product_costs[location]=new_price
                            #print new cost
                            print("Product cost has been updated")
                            print()
                            break
                        else:
                            #if the price is not valid tell user
                            print("Invalid cost!")
                else:
                    while True:
                        #asl the user for the new quantity
                        new_quantity=int(input("Enter a new quantity: "))
                        #make sure quantity is more than 0
                        if new_quantity>0:
                            location=product_names.index(update)
                            product_amount[location]=new_quantity
                            #print new quantity
                            print("Product quantity has been updated")
                            print()
                            break
                        else:
                            print("Invalid entry!")
                    
            else:
                print("Invalid option")
                print()
            
                
            
        else:
            print("Product doesn't exist. Can't update.")
            print()

    elif lowercase_answer=="e":
        #establish the max price
        biggest=max(product_costs)
        format_biggest=format(biggest,".2f")
        #estbalish min price
        smallest=min(product_costs)
        format_smallest=format(smallest,".2f")

        #edit header for max price
        format_max=format("Most expensive product:","<29s")
        print(format_max,end="")
        edited_product="("+product_names[product_costs.index(biggest)]+")"
        #print most expensive item and price
        print(format(format_biggest,"<5s"),end="")
        print(edited_product)
        
        #edit header for least expensive price
        format_min=format("Least expensive product:","<29s")
        print(format_min,end="")
        edited_product2="("+product_names[product_costs.index(smallest)]+")"
        #print least expensive item and price
        print(format(format_smallest,"<5s"),end="")
        print(edited_product2)

        #edit header for total
        format_avg=format("Total value of all products:","<29s")
        print(format_avg,end="")
        total=0
        #use loop to gain total
        for x in range(len(product_costs)):
            total+=(product_costs[x])*(product_amount[x])
        format_total=format(total,".2f")
        #print total
        print(format_total)
        print()
        
    elif lowercase_answer=="q":
        #if the user wishes to quit print a goodbye statement
        print("See you soon!")
        break
    else:
        #if the user enters an invalid answer tell them, and reprompt them
        print("Invalid option, try again")
        print()



    
