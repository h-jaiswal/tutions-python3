

def main():

    students = []

    numStudents = int(input("Enter how many students are there? "))

    for i in range(numStudents):

        # input details for a student

        student = {}

        name = input("Enter name: ")
        marks = int(input("Enter marks: "))
        standard = int(input("Enter standard (class only): "))


        # new key-value pair is added if key not already present in the dictionary
        student["name"] = name
        student["marks"] = marks 
        student["standard"] = standard

        # add the student in the students list

        students.append(student)

    for student in students:
        print(str(student))


    # for i in range(len(students)):
    #     print(str( students[i] ))

    

    for student in students:
        print("________________________________________________")
        print()

        # for value in student.values():
        #     print(value)

        for k,v in student.items():
            print( "{} - {}".format(k,v) )

        print()
        print("________________________________________________")


    # for i in range(len(students)):
    #     print("________________________________________________")
    #     print()

    #     # for value in students[i].values():
    #     #     print(value)

    #     for k,v in students[i].items():
    #         print( "{} - {}".format(k,v) )
            
    #     print()
    #     print("________________________________________________")
    



main()