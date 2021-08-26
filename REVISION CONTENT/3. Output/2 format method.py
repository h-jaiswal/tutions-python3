def main():

    # OUTRPUT firstNum + secondNum = result

    a = 10
    b = 20
    c = a + b

    print(  "The sum of {} + {} = {}".format(a, b, c)  )

    print(  "The sum of {firstNum} + {secondNum} = {result}".format(firstNum = a, secondNum = b, result = c)  )




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