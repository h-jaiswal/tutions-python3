"""

51

Using the song “10 green bottles”, 
display the lines 
“There are  str(num)] green bottles 
hanging on the wall,
 str(num)] green bottles hanging on the wall,
and if 1 green bottle 
should accidentally fall”.

Then ask the question “how many green bottles will be 
hanging on the wall?” 

If the user answers correctly, display the message “There will be 
 str(num)] green bottles hanging on the wall”. 

If they answer incorrectly, display the 
message “No, try again”     until they get it right.    

When the number of green bottles gets 
down to 0, display the message “There are no more green bottles hanging on the wall

”"""

def main():
    num = 10
    answer = -1    # setting answer to a default value 

    while( answer != num and num != 0):
        # display the poem (1 bottle breaks in the poem)
        poem = "There are " + str(num) + " green bottles\nhanging on the wall,\n" + str(num) + " green bottles hanging on the wall,\nand if 1 green bottle\nshould accidentally fall"
        print(poem)

        # ask the user for his answer  
        answer = int(input("How many green bottles will be hanging on the wall? "))

        # update value of str(num) to str(num) - 1
        num = num - 1 

        # display try again message if answer incorrect
        if( answer != num and num != 0 ):
            print("No, try again.")

    if  (num == 0):
            print("There are no more green bottles hanging on the wall")
    else:
        # if str(num) != 0 and we are out of the loop, it means that answer was correct, therefore
        print("There will be " + str(num) + "green bottles hanging on the wall")

main()


# TEST 
# 1. If you enter correct answer -> print("There will be " + str(num) + "green bottles hanging on the wall") will print

# 2. If you enter Incorrect answer continuosly -> No try again part will run UNTIL num becomes 0 and then There are no more green bottles hanging on the wall will print

# 3. If we enter incorrect answer but answer correctly before bottles become 0 ->
