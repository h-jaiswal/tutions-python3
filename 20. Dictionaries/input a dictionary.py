def main():

    # initialize a student dictionary with default values
    # default value is a starting value - or any invalid values
    student = {
        "name" : "",
        "marks" : -1,
        "standard" : -1
    }

    name = input("Enter name: ")
    marks = int(input("Enter marks: "))
    standard = int(input("Enter standard (class only): "))

    # modifies the value if key already present
    student["name"] = name
    student["marks"] = marks 
    student["standard"] = standard


    print(str(student))


main()



# def main():

#     student = {}

#     name = input("Enter name: ")
#     marks = int(input("Enter marks: "))
#     standard = int(input("Enter standard (class only): "))


#     new key-value pair is added if key not already present in the dictionary
#     student["name"] = name
#     student["marks"] = marks 
#     student["standard"] = standard


#     print(str(student))


# main()