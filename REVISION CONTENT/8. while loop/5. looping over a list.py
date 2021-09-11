def main():


    items = ['maggie', 'popcorn', 'battery', 'chips']

    index = 0

    while( index < len(items) ):
        print( items[index] )
        index = index + 1

    print()
    
    for index in range( len(items) ):
        print(items[index])



    print()

    for item in items:
        print(item)
main()