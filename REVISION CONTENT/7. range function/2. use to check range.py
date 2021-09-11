"""
If we want to check if a number N lies between START(inclusive) and END(exclusive)

ex to check  if  10 lies between   [7, 12)  i.e in range(7, 12) i.e. in {7, 8, 9, 10, 11}

    10 in range(7, 12)  expression will return TRUE if 10 lies in {7, 8, 9, 10, 11} otherwise return FALSE

"""

def main():
    num = int(input("Enter a number:"))

    # code to check if num lies in range {100, 101, 102, ............................., 999}
    # i.e. to check if num lies in range(100, 1000)     (100 inclusive, 1000 exlusive)

    # in is an operator
    if (num in range(100, 1000)):
        print("Number lies in range {100, 101, 102, ............................., 999}")
    else:
        print("Number DO NOT lies in range {100, 101, 102, ............................., 999}")

main()