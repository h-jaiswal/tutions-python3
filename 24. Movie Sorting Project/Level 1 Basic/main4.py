def keyRating(item):
    return item["rating"]

def keyTitle(item):
    return item["title"]

def keyYear(item):
    return item["year"]

def keyLength(item):
    return item["length"]

def printHeading(title):
    print("***************** {} *****************".format(title))


def printMovieList(movieList):

    print()

    for movie in movieList:
        print("Title - \t\t{}".format( movie["title"] ))
        print("Year release - \t\t{}".format( movie["year"] ))
        print("Length in minutes - \t{}".format( movie["length"] ))
        print("Average Rating - \t{}".format( movie["rating"] ))
        print()
    
    print()

def main():

    # MOVIE DATA

    movieList = [
        {
            "title" : "The Shawshank Redemption",
            "year" : 1994,    # year of release
            "length" : 142, 
            "rating" : 9.3
        },
        {
            "title" : "The Godfather",
            "year" : 1972,    # year of release
            "length" : 147, 
            "rating" : 9.2
        },
        {
            "title" : "The Dark Knight",
            "year" : 2008,    # year of release
            "length" : 152, 
            "rating" : 9
        },
        {
            "title" : "The Matrix",
            "year" : 1999,    # year of release
            "length" : 136, 
            "rating" : 8.7
        }
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
    printHeading( "Popular List" )
    printMovieList( descendingRatingList )

    # print("ascendingTitleList : {}".format( ascendingTitleList ))
    printHeading("A-Z List")
    printMovieList( ascendingTitleList )

    # print("descendingYearList : {}".format( descendingYearList ))
    printHeading("Latest Movies List")
    printMovieList( descendingYearList )

    # print("ascendingRunningTimeList : {}".format( ascendingRunningTimeList ))
    printHeading("Movies List (Increasing length)")
    printMovieList( ascendingRunningTimeList )

main()
