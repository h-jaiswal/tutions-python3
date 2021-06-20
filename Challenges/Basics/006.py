#006 
#Ask how many slices 
#of pizza the user 
#started with and ask 
#how many slices 
#they have eaten. 
#Work out how many 
#slices they have left 
#and display the 
#answer in a userfriendly format 

def main():
	numSlices = int(input("Enter number of slices: "))
	numSlicesEaten = int(input("Enter number of slices eaten: "))

	numSlicesLeft = numSlices - numSlicesEaten

	print( str(numSlicesLeft ) + " slices are left.")
main()