def main():

    # OUTRPUT firstNum + secondNum = result

    a = 10
    b = 20
    c = a + b

    print( "The sum of " + str(a) + " + " + str(b) + " = " + str(c) )   # printing long sentences with variables in between is irritating and prone to mistakes when done using + operator 

    print(  "The sum of {} + {} = {}".format(a, b, c)  )

    print(  "The sum of {0} + {1} = {2}".format(a, b, c)  )

    print(  "The sum of {firstNum} + {secondNum} = {result}".format(result = c, secondNum = b, firstNum = a)  )

    # more examples ->
    #  The sum of 10 + 10 = 30
    print(  "The sum of {firstNum} + {firstNum} = {result}".format(firstNum = a, result = c)  )
    
    # Siddharth is a boy. Siddharth likes blue. Siddharth hates red.
    name = "Siddharth"
    color1 = "blue"
    color2 = "red"
    gender = "boy"

    print("{} is a {}. {} likes {}. {} hates {}.".format(name, gender, name, color1, name, color2))

    print("{0} is a {1}. {0} likes {2}. {0} hates {3}.".format(name, gender, color1, color2))

    print("{name} is a {gender}. {name} likes {color1}. {name} hates {color2}".format(name = name, gender = gender, color1 = color1, color2 = color2) )



    #
    name = "Harshit"
    marks = 87

    print( "{} has scored {} marks.".format(name, marks) )

    print( "{name} has scored {score} marks.".format(name = name, score = marks) )




    # other ways to use format method

    # using indexing 
    print(  "The sum of {0} + {1} = {2}".format(a, b, c)  )

    #
    print(  "The sum of {a} + {b} = {c}".format(a=a, b=b, c=c)  )



    print( "{1} has scored {0} marks.".format(marks, name) )

    print( "{0} has scored {1} marks.".format(name, marks) )

    print( "{name} has scored {marks} marks.".format(name = name, marks = marks) )



if __name__ == "__main__" :
    main()