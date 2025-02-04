
listnum = int(input("How many lists?: "))

biglist = [input(f"Enter Values for list {i+1}: ").split() for i in range(listnum)]

lastitem_list =  []
lastitem_list = [lastitem_list + [(biglist)[i][-1]] for i in range(listnum)]

print (lastitem_list)
