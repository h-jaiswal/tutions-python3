def main():
    # Using * operator with list

    # list1 = ["Pen", "Notebook"] * 3

    # print(str(list1)) 

    # Example

    attendance = ["Absent"] * 10

    print(str(attendance))

    for rollno in range( 1, 11):

        status = input( "Roll no {} is Present?: ".format(rollno) )

        if(status == "Present"):
            attendance[rollno-1] = "Present"

        print(str(attendance))

main()