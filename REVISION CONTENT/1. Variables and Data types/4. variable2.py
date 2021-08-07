def main():

    a = [1,2, 3]

    a2 = list( [1, 2, 3] )

    a3 = list( (1, 2, 3) )

    print( type(a) )
    print( type(a2) )
    print( type(a3) )

    b = (1,2,3)

    b2 = tuple( [1,2,3] )

    b3 = tuple( (1, 2, 3) )

    print( type(b) )
    print( type(b2) )
    print( type(b3) )

    c = {
        'name' : 'Rishav',
        'age'  : 14
     }

    print( type(c) )

if __name__ == "__main__":
    main()
