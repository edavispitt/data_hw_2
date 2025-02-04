intlist = input("Enter your list of integers:").split()

for i in range(len(intlist)):
    intlist[i] = int(intlist[i])
    intlist[i] = intlist[i] + 1

print (intlist)
