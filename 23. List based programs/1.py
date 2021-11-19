

def main():

    # Example of List of lists

    numOfStudents = int( input("Enter number of students: ") )

    students = []

    for i in range( numOfStudents ):
        
        # 1 INPUT a student

        # input student details
        name = input("Enter name: ")
        marks = int( input("Enter marks out of 100: ") )

        if (name == ""):
            name = "Not Set"
        if (marks > 100 or marks < 0):
            marks = -1
        ##student = []
        ##student.append(name)
        ##student.append(marks)

        student = [name, marks]



        # 2 ADD STUDENT to STUDENT LIST
        students.append(student)
        #students.append( [name, marks] )

    print(students)

main()