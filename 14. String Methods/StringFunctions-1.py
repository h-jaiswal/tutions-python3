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



    # len( name )
    # returns number of characters in the string including alphabets, space, numbers, special character, etc. 

    print( len(name) )

    print( len( name.strip(" ") ) )

    print( len("Rishav") ) 


    print( "Number of characters in variable name : " + str( len(name) ))
main()