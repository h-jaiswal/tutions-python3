def main():

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

main()