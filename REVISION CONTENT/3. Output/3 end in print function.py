def main():


    # below three print statements will print in three separate lines
    # because default end character/string is "\n" i.e. new line

    print("Hello")
    print("hi")
    print("Namaste")
    

    # we can change default end character/string to any thing we want

    # Hello, hi, Namaste\n

    print("Hello" , end=", ")
    print("hi"  , end=", ")
    print("Namaste"  , end="\n")



    # Hello Hi Namaste.
    #
    print("Hello", end=" ")
    print("Hi", end=" ")
    print("Namaste", end=".\n")


    # Date print 

    # 5/June/2021
    #
    print(5, end="/")
    print("June", end="/")
    print(2021)

main()