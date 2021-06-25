def keyRating(item):
    return item["rating"]

def keyTitle(item):
    return item["title"]

def keyYear(item):
    return item["year"]

def keyLength(item):
    return item["length"]

def main():

    # MOVIE DATA

    # input from terminal

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


    # manual input in code
    
    # movieList = [
    #     {
    #         "title" : "The Shawshank Redemption",
    #         "year" : 1994,    # year of release
    #         "length" : 142, 
    #         "rating" : 9.3
    #     },
    #     {
    #         "title" : "The Godfather",
    #         "year" : 1972,    # year of release
    #         "length" : 147, 
    #         "rating" : 9.2
    #     },
    #     {
    #         "title" : "The Dark Knight",
    #         "year" : 2008,    # year of release
    #         "length" : 152, 
    #         "rating" : 9
    #     },
    #     {
    #         "title" : "The Matrix",
    #         "year" : 1999,    # year of release
    #         "length" : 136, 
    #         "rating" : 8.7
    #     }
    # ]


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
        print("Title - \t\t{}".format( movie["title"] ))
        print("Year release - \t\t{}".format( movie["year"] ))
        print("Length in minutes - \t{}".format( movie["length"] ))
        print("Average Rating - \t{}".format( movie["rating"] ))
        print()
    
    print()

    # print("ascendingTitleList : {}".format( ascendingTitleList ))

    print("***************** A-Z List *****************")
    
    print()

    for movie in ascendingTitleList:
        print("Title - \t\t{}".format( movie["title"] ))
        print("Year release - \t\t{}".format( movie["year"] ))
        print("Length in minutes - \t{}".format( movie["length"] ))
        print("Average Rating - \t{}".format( movie["rating"] ))
        print()
    
    print()
    

    # print("descendingYearList : {}".format( descendingYearList ))

    print("***************** Latest Movies List *****************")
    
    print()

    for movie in descendingYearList:
        print("Title - \t\t{}".format( movie["title"] ))
        print("Year release - \t\t{}".format( movie["year"] ))
        print("Length in minutes - \t{}".format( movie["length"] ))
        print("Average Rating - \t{}".format( movie["rating"] ))
        print()
    
    print()
    

    # print("ascendingRunningTimeList : {}".format( ascendingRunningTimeList ))

    
    print("***************** Movies List (Increasing length) *****************")
    
    print()

    for movie in ascendingRunningTimeList:
        print("Title - \t\t{}".format( movie["title"] ))
        print("Year release - \t\t{}".format( movie["year"] ))
        print("Length in minutes - \t{}".format( movie["length"] ))
        print("Average Rating - \t{}".format( movie["rating"] ))
        print()
    
    print()

main()
