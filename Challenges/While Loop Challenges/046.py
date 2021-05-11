"""
046 
Ask the user to enter 
a number. Keep 
asking until they enter 
a value over 5 and 
then display the 
message “The last 
number you entered 
was a [number]” and 
stop the program. 
"""

def main():

    val = int(input("Enter a value: "))
    while(val <= 5):  # loop running condition is val <= 5 
        val = int(input("Enter a value: "))
    print("The last number you entered was a " + str(val))
main()