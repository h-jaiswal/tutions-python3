"""
045 
Set the total to 0 to start with. 

While the total is 50 or less,
    ask the user to input a number. 
    Add that number to the total and 
    print the message “The total is… [total]”. 

Stop the loop when 
the total is over 50. 

"""
def main():
    print("Program will run until total <= 50\n")

    total = 0
    while( total <= 50 ):
        num = int( input("Enter a value: ") )
        total = total + num
        print("The current total is : " + str(total))
    
    print("\nThe final total is: " + str(total))

main()