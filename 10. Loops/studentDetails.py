"""
Enter details(name, roll no) of n number of stundents. ask the number of students from user
"""

def main():
    numStudents = int(input("Please enter no. of students: "))

    i = 1
    while( i <= numStudents ):
        name = input("Enter name: ")
        rollNo = int(input("Enter roll no: "))

        print( str(rollNo) + " " + name )
        i = i + 1

    # print("You have entered: ")

    # i = 1
    # while( i <= numStudents ):
    #     print( str(rollNo) + " " + name )
    #     i = i + 1
    
    # print("Thanks for using the program.")

main()