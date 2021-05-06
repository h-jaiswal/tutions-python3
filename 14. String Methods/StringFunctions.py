def main():

    sentence = input("Enter a string i.e. sentence: \n")

    print( sentence ) # prints orignal value of sentence
    print()


    print("Converting to  lowercase - ")

    print( sentence.lower() )  # .lower() converts value of sentence to lowercase, orginial value of sentence remains unchanged
    print()

    print("Converting to  capitalize - ")

    print( sentence.capitalize() )
    print()


    print("Converting to  upper case - ")

    print( sentence.upper() )
    print()


    print("Converting to  title case - ")

    print( sentence.title() )
    print()


main()