"""
50 

Ask the user to enter a number between 
10 and 20. 

If they enter a value under 10, 
display the message “Too low” and ask 
them to try again. 

If they enter a value 
above 20, display the message “Too high” 
and ask them to try again. 

Keep repeating 

this until they enter a value that is 
between 10 and 20  (loop_stopping condition)

and then display the 
message “Thank you”

HINT : loop_running_condition = not(loop_stopping condition)

"""

def main():
    num = int(input("Enter a number: "))

    while not( 10 < num and num < 20 ):  # HINT : loop_running_condition = not(loop_stopping condition)
        if( num < 10 ):
            print("Too low.")
        elif ( num > 20 ):
            print("Too high.")

        num = int(input("Enter a number: "))
    
    print("Thank you")

main()