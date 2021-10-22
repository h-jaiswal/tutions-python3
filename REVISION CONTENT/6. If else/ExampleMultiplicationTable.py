def main():
    num = int(input("Enter a number: "))   
    # for loop  # value of times will range from 1, 2, 3, .. upto 10
    for times in range(1, 10 + 1 ): 
        result = num * times
        print("{} * {} = {}".format(num, times, result))
main()