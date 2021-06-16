def keyRating(item):
    return item[3]

def keyTitle(item):
    return item[0]

def keyYear(item):
    return item[1]

def keyLength(item):
    return item[2]
def main():

    # MOVIE DATA

    movieList = [
        ["The Shawshank Redemption", 1994, 142, 9.3],
        ["The Godfather", 1972, 147, 9.2],
        ["The Dark Knight", 2008, 152, 9],
        ["The Matrix", 1999, 136, 8.7]
    ]

    # SORT

    # sort in decreasing order of Rating (Most popular first)

    descendingRatingList = sorted( movieList, reverse = True, key = keyRating )

    # sort in increasing order of Title (A-Z)

    ascendingTitleList = sorted( movieList, key = keyTitle )

    # sort in decreasing order of year (latest movies first)
    
    descendingYearList = sorted( movieList, reverse = True, key = keyYear )

    # sort in increasing order of length (minutes.  Shortest running time movie first)

    ascendingRunningTimeList = sorted( movieList, key = keyTitle )



    # OUTPUT / DISPLAY
    
    # print("descendingRatingList : {}".format( descendingRatingList ))

    print("***************** Popular List *****************")
    
    print()

    for movie in descendingRatingList:
        print("Title - \t\t{}".format( movie[0] ))
        print("Year release - \t\t{}".format( movie[1] ))
        print("Length in minutes - \t{}".format( movie[2] ))
        print("Average Rating - \t{}".format( movie[3] ))
        print()
    
    print()

    # print("ascendingTitleList : {}".format( ascendingTitleList ))

    print("***************** A-Z List *****************")
    
    print()

    for movie in ascendingTitleList:
        print("Title - \t\t{}".format( movie[0] ))
        print("Year release - \t\t{}".format( movie[1] ))
        print("Length in minutes - \t{}".format( movie[2] ))
        print("Average Rating - \t{}".format( movie[3] ))
        print()
    
    print()
    

    # print("descendingYearList : {}".format( descendingYearList ))

    print("***************** Latest Movies List *****************")
    
    print()

    for movie in descendingYearList:
        print("Title - \t\t{}".format( movie[0] ))
        print("Year release - \t\t{}".format( movie[1] ))
        print("Length in minutes - \t{}".format( movie[2] ))
        print("Average Rating - \t{}".format( movie[3] ))
        print()
    
    print()
    

    # print("ascendingRunningTimeList : {}".format( ascendingRunningTimeList ))

    
    print("***************** Movies List (Increasing length) *****************")
    
    print()

    for movie in ascendingRunningTimeList:
        print("Title - \t\t{}".format( movie[0] ))
        print("Year release - \t\t{}".format( movie[1] ))
        print("Length in minutes - \t{}".format( movie[2] ))
        print("Average Rating - \t{}".format( movie[3] ))
        print()
    
    print()

main()
