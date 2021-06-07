def main():

    print(  "Harshit"  ,  "Rishav"   )    # print with more than 1 argument 

    print(  "Harshit" + " " + "Rishav"  )   # print with only 1 argument


    # BOTH above prints  Harshit Rishav


    # default separator is a single space if we provide more than 1 argument to print function

    print( "Hi", "my", "name", "is", "Harshit")   # print with 5 arguments


    print( "Hi", "my", "name", "is", "Harshit", sep = ", ")   # print with 5 arguments


    print( "Hi", "my", "name", "is", "Harshit", sep = " -- ")   # print with 5 arguments

    

    # both sep and end can be used in same print function


    print(  "Harshit" , " Age: 21 " , sep = " --> " , end = "\t")
    print(  "Rishav" , " Age: 14 " , sep = " --> " , end = "\t")

main()