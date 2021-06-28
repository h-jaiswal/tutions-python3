"""
Loop - in eng means - "a series of instructions" that is repeated until a particular thing happens.

Loop in python - 
Two types- 1. while loop (basic loop) 2. for loop (advanced loop)

WHILE LOOP

while( loop_running_condition ):
    one or more statement(s) which are to be repeated

Here, while is a python keyword (like print, main, in, or, and etc.) 
loop_running_condition can be any condition that gives either True or False

How it works? The statements inside while loop are repeated until the loop condition becomes false

example:
print my name for 10 times

name = "Harshit Jaiswal"

i = 1   # loop varible, it's value will be different for each loop run

while( i <= 10 ):
    print(name)
    i = i + 1  # this is called loop variable update statement
print("Bye")

WORKING EXPLAINED below
i = 1, 1 <= 10 is true (loop condition is  true) -> print("Harshit Jaiswal"), i = 1 + 1 = 2

again loop condition is checked for updated value of loop variable, here i
i = 2, 2 <= 10 is true (loop condition is  true) -> print("Harshit Jaiswal"), i = 2 + 1 = 3

again loop condition is checked for updated value of loop variable, here i
i = 3, 3 <= 10  is true (loop condition is  true) -> print("Harshit Jaiswal"), i = 3 + 1 = 4

.
.
.
.
.
. 

again loop condition is checked for updated value of loop variable, here i
i = 10, 10 <= 10  is true (loop condition is  true) -> print("Harshit Jaiswal"), i = 10 + 1 = 11

again loop condition is checked for updated value of loop variable, here i
i = 11, 11 <= 10 is FALSE (loop condition is  False) -> Loop will end, and statement after loop will be run.

"""

name = "Harshit Jaiswal"

i = 1   # loop varible, it's value will be different for each loop run

while( i <= 10 ):
    print( str(i) + " " + name)
    i = i + 1  # this is called loop variable update statement
print("Bye") 