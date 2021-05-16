"""
49 
Create a variable called 
compnum
and set the value 
to 50.

Ask the user to enter a 
number.

While their guess 
is not the same as the 
compnum value, 

tell them if 
their guess is too low or too 
high and ask them to have 
another guess. 

If they enter 
the same value as 
compNum, display the 
message “Well done, you 
took [count] attempts”. 

"""

def main():
    print("A simple guessing game made using python\n")

    compNum = 50
    guessNum = int(input("Enter a number: "))

    score = 0
    while( compNum != guessNum ):
        if( guessNum < compNum ):
            print("Too Low")
        else:
            print("Too high")
        
        guessNum = int(input("Wrong guess, try once more: "))
        score = score + 1

    # if above ends, it will mean that guessNum and compNum have equal values
    print("Well done, you took " + str(score) + " attempts")

main()