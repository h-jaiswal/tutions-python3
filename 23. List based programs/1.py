

def main():

    # Example of List of lists

    numOfStudents = int( input("Enter number of students: ") )

    students = []

    for i in range( numOfStudents ):

        # input student details
        name = input("Enter name: ")
        marks = int( input("Enter marks out of 100: ") )

        if (name == ""):
            name = "Not Set"
        if (marks > 100 or marks < 0):
            marks = -1
        
        students.append( [name, marks] )

    print(students)

main()