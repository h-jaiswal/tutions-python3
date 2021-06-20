"""Create a tuple containing the names of five countries 

and display the whole tuple.

Ask the user to enter one of the countries 

that have been shown to them and 

then display 
the index number (i.e. position in the list) of that item in the tuple. """


def main():

    countries = ( "India", "Japan", "Malaysia", "Rangoon", "Germany" )
    
    # to display a whole tuple or a list, we can simply print it using its variable

    print( "All 5 country names are: " + str(countries))

    country = input("Enter a country name from the given collection above: ")

    index = countries.index( country )

    print(index)

main()