def main():
    T = int(input())
    while T > 0:
        n, x = [int(x) for x in input().split()]
        A = {}
        numKeys = 0
        for temp in [int(x) for x in input().split()]:
            if temp in A.keys():
                A[temp] += 1
            else:
                A[temp] = 1
                numKeys += 1

        if numKeys >= n-x:
            print(n-x)
        else:
            print(numKeys)
    T -= 1
main()