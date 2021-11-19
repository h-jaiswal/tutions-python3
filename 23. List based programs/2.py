def main():
    
    # Example - Preparing ranklist (sorting in ascending order on basis of marks)

    students = [
        ["Piyush", 100],
        ["Bhavesh", 69],
        ["Joseph", 45],
        ["Abhi", 69],
        ["Rishav", 10]
    ]   
    # ONLY MARKS
    print( sorted( students, key = keyMarks, reverse=True ) )
    print()
    #print(students)

    # Example - Attendance list (sorting in ascending order on basis of name)

    # ONLY NAME
    print( sorted( students, key = keyNames ) )
    print()

    # FIRST SORTING (DESC) On basis of marks AND then sorting (ASCE) on basis of name



def keyNames(item):
    return item[0]

def keyMarks(item):
    return item[1]

main()
