
names = []   # names list

n = int(input("How many names? : "))

for i in range(n):   # loop will repeat n times
    name = input()
    names.append(name)

# advanced for loop (for loop in combination with list)
for name in names:
    print(name)