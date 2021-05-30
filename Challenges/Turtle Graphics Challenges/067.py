"""067 
Run the following pattern: 
10 Octagons inclined to each other at 36 degrees
"""


import turtle

def main() :
    for x in range(10):
        # octagon
        for i in range(8):
            turtle.forward(50)
            turtle.right(45)
        
        # turn the next octagon
        turtle.right(36)
    
    turtle.hideturtle()
    turtle.exitonclick()

main()