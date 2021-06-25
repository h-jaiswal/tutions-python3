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

def inputMovieList():
    movieList = []

    numMovies = int(input("Enter number of movies? "))

    for i in range(numMovies):

        # movie input
        movie = {}
        
        print("Enter movie details.")

        # title = input("Enter movie title: ")
        # movie["title"] = title

        movie["title"] = input("Enter movie title: ")
        movie["year"] = input("Enter year of relase: ")
        movie["length"] = input("Enter length of movie in minutes: ")
        movie["rating"] = input("Enter average rating: ")

        # add to list
        movieList.append(movie)

    return movieList

def main():

    # MOVIE DATA
    movieList = inputMovieList()

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
