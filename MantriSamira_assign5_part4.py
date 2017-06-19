#Samira Mantri 3/15/16 section-3 MantriSamira_assign5_part4.py


#Pattern 1

# draw a cube at the edge of each axis

#draw cubes on x axis
for x in range(-500, 501, 50):
	# use loop to adjust x position
	cube(x, 0, 0)

#draw cubes on z axis
for z in range(-500,501,50):
	# use loop to adjust z position
	cube(0,0,z)

#draw cubes on y axis
for y in range(0,501,50):
	#use a loop to adjust y position
	cube(0,y,0)


#Pattern 2

#set the original lengths of x and z
x=10
z=10
#create for loop in order for y to gradually increase for the first half of
#the diamond
for y in range(10,250,10):
	cube(0, y, 0, x, 10, z)
	#make sure that 10 is added to x and z in order for
	#the side lengths to increase
	x+=10
	z+=10

#set x and z equal to the number they were by the end of the last loop
x=250
z=250
#create for loop in order for y to gradually increase during the second half
# of the diamond
for y in range(250,501,10):
	cube(0, y, 0, x, 10, z)
	#make sure that 10 is subtracted from x and z in order
	#for the side lenths to gradually decrease
	x-=10
	z-=10

#Pattern 3

#create the base of the tree
for y in range(0,101,50):
	cube(0,y,0)

#create the top part of the tree
#set x and z equal to 300 so they are equally subtracted and create a
#an even tree
x=300
z=300
#create for loop in order for y to gradually increase to create the second
#half of the tree
for y in range(111,411,10):
	cube(0, y, 0, x, 10, z)
	#make sure that 10 is subtracted from x and z in order
	#for the side lengths to gradually decrease since the tree
	#gets smaller as you get closer to the top
	x-=10
	z-=10

#Pattern 4

#set the range for x
for x in range(-500,501,50):
		#create a cube to form the base
		cube(x,0,0,50,50,50)
		#use variable to alter the size of the cube as y grows
		size=50
		#set the range for y
		for y in range(50,501,50):
			#create the cube that will gradually become smaller
			cube(x,y,0,size,size,size)
			#make sure to minus 5 each time from the size of
			#the cube to diminish its size
			size-=5
