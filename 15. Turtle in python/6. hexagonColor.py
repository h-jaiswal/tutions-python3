import turtle

def main():
    sidesValue = 3
    angleValue = 120
    sideLengthValue = 200
    turtle.color('red', 'blue')
    turtle.begin_fill()
    for i in range(sidesValue):
        turtle.forward(sideLengthValue)
        turtle.left(angleValue) 
    turtle.end_fill()
    turtle.done()

main()
