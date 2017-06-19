#Samira Mantri 2/10/16 section:3 MantriSamira_assign3_problem1.py

#Print the name of the program
print("Valid Triangle Tester")
print()
#Prompt the user to input 3 x and y coordinates
#Make sure these inputs are floating numbers
x1=float(input("Enter Point #1 - x position: "))
y1=float(input("Enter Point #1 - y position: "))
x2=float(input("Enter Point #2 - x position: "))
y2=float(input("Enter Point #2 - y position: "))
x3=float(input("Enter Point #3 - x position: "))
y3=float(input("Enter Point #3 - y position: "))
print()

#Calculate the lengths of the sides
side1=((x1-x2)**2+(y1-y2)**2)**0.5
side2=((x3-x1)**2+(y3-y1)**2)**0.5
side3=((x2-x3)**2+(y2-y3)**2)**0.5

#format the sides to two decimal places
format_side1=format(side1,".2f")
format_side2=format(side2,".2f")
format_side3=format(side3,".2f")

#print the lengths of the sides
print("The length of each side of your test shape is:")
print()
print("Side 1:",format_side1)
print("Side 2:",format_side2)
print("Side 3:",format_side3)
print()

#Use boolean expressions to find out and print whether the sides do, or do not
#form a valid triangle

if side1+side2>side3 and side2+side3>side1 and side3+side1>side2:
    print("This is a valid triangle!")
    #Use boolean expressions to discover if the triangle is equilateral
    if format_side1==format_side2 and format_side2==format_side3 and format_side3==format_side1:
        print("This is an equilateral triangle")
        #import turtle
        import turtle
        #set up graphical canvas
        #width=500 and height=500
        turtle.setup(500,500)
        #move turtle to the first point
        turtle.penup()
        turtle.goto(x1,y1)
        #adjust pen thickness
        turtle.pensize(7)
        #set the fill color
        turtle.fillcolor("blue")
        #tell python to start filling
        turtle.pendown()
        turtle.begin_fill()
        #draw a line connecting the points
        turtle.goto(x2,y2)
        turtle.goto(x3,y3)
        turtle.goto(x1,y1)
        #tell turtle to stop filling
        turtle.end_fill()
    #Use boolean expressions to discover if the triangle is isosceles
    elif format_side1==format_side2 and format_side2!=format_side3:
        print("This is an isosceles triangle")
        #import turtle
        import turtle
        #set up graphical canvas
        #width=500 and height=500
        turtle.setup(500,500)
        #move turtle to the first point
        turtle.penup()
        turtle.goto(x1,y1)
        #adjust pen thickness
        turtle.pensize(7)
        #set the fill color
        turtle.fillcolor("yellow")
        #tell python to start filling
        turtle.pendown()
        turtle.begin_fill()
        #draw a line connecting the points
        turtle.goto(x2,y2)
        turtle.goto(x3,y3)
        turtle.goto(x1,y1)
        #tell turtle to stop filling
        turtle.end_fill()
    elif format_side2==format_side3 and format_side3!=format_side1:
        print("This is an isosceles triangle")
        #import turtle
        import turtle
        #set up graphical canvas
        #width=500 and height=500
        turtle.setup(500,500)
        #move turtle to the first point
        turtle.penup()
        turtle.goto(x1,y1)
        #adjust pen thickness
        turtle.pensize(7)
        #set the fill color
        turtle.fillcolor("yellow")
        #tell python to start filling
        turtle.pendown()
        turtle.begin_fill()
        #draw a line connecting the points
        turtle.goto(x2,y2)
        turtle.goto(x3,y3)
        turtle.goto(x1,y1)
        #tell turtle to stop filling
        turtle.end_fill()
    elif format_side3==format_side1 and format_side1!=format_side2:
        print("This is an isosceles triangle")
        #import turtle
        import turtle
        #set up graphical canvas
        #width=500 and height=500
        turtle.setup(500,500)
        #move turtle to the first point
        turtle.penup()
        turtle.goto(x1,y1)
        #adjust pen thickness
        turtle.pensize(7)
        #set the fill color
        turtle.fillcolor("yellow")
        #tell python to start filling
        turtle.pendown()
        turtle.begin_fill()
        #draw a line connecting the points
        turtle.goto(x2,y2)
        turtle.goto(x3,y3)
        turtle.goto(x1,y1)
        #tell turtle to stop filling
        turtle.end_fill()
    #Use a boolean expression to discover if the triangle is scalene
    else:
        print("This is a scalene triangle")
        #import turtle
        import turtle
        #set up graphical canvas
        #width=500 and height=500
        turtle.setup(500,500)
        #move turtle to the first point
        turtle.penup()
        turtle.goto(x1,y1)
        #adjust pen thickness
        turtle.pensize(7)
        #set the fill color
        turtle.fillcolor("green")
        #tell python to start filling
        turtle.pendown()
        turtle.begin_fill()
        #draw a line connecting the points
        turtle.goto(x2,y2)
        turtle.goto(x3,y3)
        turtle.goto(x1,y1)
        #tell turtle to stop filling
        turtle.end_fill()

else:
    print("This is not a valid triangle")


    
    



    
