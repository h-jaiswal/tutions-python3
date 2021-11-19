"""
    student = {
        # "name" : "Harshit Jaiswal"

        "name" : {
            "firstName" : "Harshit",
            "middleName" : "",
            "lastName" : "Jaiswal",
            "userName" : "farrago"
        },

        # "age" : 21

        "dateOfBirth" : {
            "day" : 30,
            "month": 3,
            "year" : 2000
        },

        # "standard" : 7 

        "stardard" : {
            "class" : 7,
            "section" : "A"
        },      

        marks : 96,

        # # -1 means Absent on test day
        # marks : [10, 94, 78, -1, 76]

        # -1 means Absent on test day
        # "marks": {
            "maths" : 10,
            "science" : 94,
            "english" : 78,
            "social" : -1,
            "hindi" : 76
        }
    }
    
"""

from datetime import date

def main():

    # Creating the student dict. (empty)
    student = {}

    # Input 1st key of student dict
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


    # Input 2nd key of student dict

    dateOfBirth = {}

    print("Enter date of birth details")
    dateOfBirth["day"] = int(input("Enter day: "))
    dateOfBirth["month"] = int(input("Enter month: "))
    dateOfBirth["year"] = int(input("Enter year: "))


    # add a new key-value pair to student dictionary
    student["dateOfBirth"] = dateOfBirth


    # Input 3rd key of student dict

    # calucate age from dateOfBirth

    currentYear = date.today().year

    # age = currentYear - (student["dateOfBirth"])["year"]
    age = currentYear - dateOfBirth["year"]

    # add a new key-value pair to student dictionary
    student["age"] = age 



    # Input 4th key of student dict

    standard = {}

    print("Enter current class details")

    standard["class"] = int(input("Enter your current class standard: "))
    standard["section"] = input("Enter section: ")
    
    # add a new key-value pair to student dictionary
    student["standard"] = standard 

    # Input 5th key of student dict

    marks = input("Enter average marks: ")
    
    # add a new key-value pair to student dictionary
    student["marks"] = marks 


    for key,value in student.items():
        print("{} - {}".format(key,value))
    

main()