def main():
    
    # below three print statements will print in three separate lines
    # because default end character/string is "\n" i.e. new line

    print("Hello")
    print("hi")
    print("Namaste")


    # we can change default end character/string to any thing we want

    
    print("Hello" , end=", ")
    print("hi"  , end=", ")
    print("Namaste"  , end="\n")


    print(5, end="/")
    print("June", end="/")
    print(2021)
main()