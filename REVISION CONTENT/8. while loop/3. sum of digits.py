def main():
    
    # sum of all digits
    
    num = 12345
    
    sum = 0 # no digit included in sum therefore, sum = 0
    while ( num != 0):
        lastDigit  = num % 10

        sum = sum + lastDigit

        num = num // 10

    print(sum)

main()