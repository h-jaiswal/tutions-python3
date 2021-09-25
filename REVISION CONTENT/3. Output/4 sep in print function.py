def main():

    # sep or separator conecept is ONLY applicable in case print function having more than 1 argument

    print( "Harshit" , "Rishav" )    # print with more than 1 argument 

    print(  "Harshit" + " " + "Rishav"  )   # print with only 1 argument

    # BOTH above prints  Harshit Rishav





    # default separator is a single space if we provide more than 1 argument to print function

    print( "Hi", "my", "name", "is", "Harshit")   # print with 5 arguments
    # Hi my name is Harshit

    print( "Hi", "my", "name", "is", "Harshit", sep = ", ")   # print with 5 arguments
    # Hi, my, name, is, Harshit

    print( "Hi", "my", "name", "is", "Harshit", sep = " -- ")   # print with 5 arguments
    # Hi -- my -- name -- is -- Harshit
    

    # both sep and end can be used in same print function

    print(  "Harshit" , " Age: 21 ")  #  default sep is single blank space and default end is newline is used

    print(  "Harshit" , " Age: 21 " , sep = " --> " , end = "\t")
    
    print(  "Harshit" , " Age: 21 " , end = "\t", sep = " --> " )

    print(  "Rishav" , " Age: 14 " , sep = " --> " , end = "\t")

main()