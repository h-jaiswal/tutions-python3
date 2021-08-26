def main():

    # check if student is topper from jabalpur
    # any student is topper if marks > 98

    # list of dictionaries
    students = [
        {
            'name' : "Harshit Jaiswal",
            'age' : 16,
            'marks' : 98.7,
            'location' : "Jabalpur"
        },
        {
            'name' : "Akash Jaiswal",
            'age' : 16,
            'marks' : 97.7,
            'location' : "Pune"
        },
        {
            'name' : "Mohit Unayal",
            'age' : 16,
            'marks' : 99.7,
            'location' : "Jabalpur"
        }
    ]


    for student in students:

        location = student['location']

        if ( location == "Jabalpur" ):
            marks = student['marks']

            if( marks > 98 ):
                name = student['name']

                print("{} is a topper from Jabalpur. Marks = {}".format(name, marks))


main()