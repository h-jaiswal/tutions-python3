def main():

    var = "Harshit Jaiswal"
    var1 = 23
    var2 = 23.5
    var3 = True
    var4 = [1,2,3]
    var5 = (1,2,3)
    var6 = {
        'name' : "Harshit Jaiswal",
        'age' : 23
    }

    print( var )
    print( var1 )
    print( var2 )
    print( var3 )
    print( var4 )
    print( var5 )
    print( var6 )


    print( "Harshit Jaiswal" )

    print( 2 )

    print( 2+3-8 ) # prints return value of expression

    print( max(10, 30) )  # will print whatever value is returned by the max function


    # string concatenation using + operator 

    print(2+3)

    print("Hello" + "World")

    print("Hi" + str(5) )

    print( str(5) + "Hi")

    # print( int("Hi") + 5)

    print( "Expression result = " + str(2+3-8) )


    name = "Harsh"
    marks = 87
    # print( name + " has scored " + marks + " marks. Great!"  )

    print( name + " has scored " + str(marks) + " marks. Great!" )




if __name__ == "__main__" :
    main()