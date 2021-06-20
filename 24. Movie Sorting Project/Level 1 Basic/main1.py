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
    
    print("descendingRatingList : {}".format( descendingRatingList ))

    print("ascendingTitleList : {}".format( ascendingTitleList ))

    print("descendingYearList : {}".format( descendingYearList ))

    print("ascendingRunningTimeList : {}".format( ascendingRunningTimeList ))


main()


