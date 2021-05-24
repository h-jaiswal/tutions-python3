import turtle

def main():
    sidesValue = 3
    angleValue = 120
    turtle.color('red', 'blue')
    turtle.begin_fill()
    for i in range(sidesValue):
        turtle.forward(angleValue)
        turtle.left(60)
    turtle.end_fill()
    turtle.done()

main()
