# lower()
# capitalize()
# upper()
# title()

def main():
    name = input()

    print(name)

    # name.strip(" ")
    # removes extra space before start and after end
    print( name.strip(" ") )

    print( name )

    name = name.strip()

    print( name )

    # len( name )
    # returns number of characters in the string including alphabets, space, numbers, special character, etc. 

    print( len(name) )

    print( len( name.strip(" ") ) )

    print( len("Rishav") ) 


    print( "Number of characters in variable name : " + str( len(name) ))






    name = input("enter a string: ")

    print(name)  # harshit jaiswal

    # always remember, in coding, couting starts from 0 and it is called

    # variable_name[start_index: end_index + 1] will give a part of the complete string stored in the variable_name 

    first_name = name[0: 7]

    print(first_name)

    # last_name = name[8 : 14]
    # above gives only jaiswa

    last_name = name[8 : ]
    # this will give part of whole string starting from given start index i.e. 8 upto last character

    print( last_name )

    print( name[6: ] )  # gives part of name string from index 6 upto last character

    print( name[2 : 11])  # gives part of name string from index 2 upto 1 index before 11 ie. from index 2 upto index 10


    # one more trick
    # reverse
    name = "Rishav"
    print( name[-1: :-1] )   # will return reverse of the complete string






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