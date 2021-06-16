def main():
    
    # Example - Preparing ranklist (sorting in ascending order on basis of marks)

    students = [
        ["Piyush", 100],
        ["Shivam", 69],
        ["Joseph", 45],
        ["Vinay", 89],
        ["Rishav", 10]
    ]   

    print( sorted( students, key = keyMarks ) )


    # Example - Attendance list (sorting in ascending order on basis of name)
    

    print( sorted( students, key = keyNames ) )
    

def keyNames(item):
    return item[0]

def keyMarks(item):
    return item[1]

main()
