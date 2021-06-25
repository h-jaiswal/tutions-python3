
def main():

    students = []
    numStudents = int(input("Enter how many students are there? "))


    # input students

    for i in range(numStudents):

        # input details for a student

        student = {}

        name = {}


        # firstName = input("Enter first name: ")
        # name["firstName"] = firstName

        name["firstName"] = input("Enter first name: ")

        while(len(name["firstName"]) == 0 ):
            print("First name cannot be empty.")
            name["firstName"] = input("Enter first name: ")

        
        name["middleName"] = input("Enter middle name (leave empty if not applies) : ")
        name["lastName"] = input("Enter last name: ")
        name["userName"] = input("Enter username: ")

        while(len(name["userName"]) < 8 ):
            print("Username should minimum 8 character long.")
            name["userName"] = input("Enter username: ")

        
        # add a new key-value pair to student dictionary
        student["name"] = name



        dateOfBirth = {}

        print("Enter date of birth details")
        dateOfBirth["day"] = int(input("Enter day: "))
        dateOfBirth["month"] = int(input("Enter month: "))
        dateOfBirth["year"] = int(input("Enter year: "))


        # add a new key-value pair to student dictionary
        student["dateOfBirth"] = dateOfBirth



        # calucate age from dateOfBirth

        currentYear = date.today().year

        # age = currentYear - (student["dateOfBirth"])["year"]
        age = currentYear - dateOfBirth["year"]

        # add a new key-value pair to student dictionary
        student["age"] = age 




        standard = {}

        print("Enter current class details")

        standard["class"] = int(input("Enter your current class standard: "))
        standard["section"] = input("Enter section: ")
        
        # add a new key-value pair to student dictionary
        student["standard"] = standard 


        marks = input("Enter average marks: ")
        
        # add a new key-value pair to student dictionary
        student["marks"] = marks 


        # add to students list

        students.append(student)

    for student in students:
        print("________________________________________________")
        print()

        # for value in student.values():
        #     print(value)

        for k,v in student.items():
            print( "{} - {}".format(k,v) )

        print()
        print("________________________________________________")

