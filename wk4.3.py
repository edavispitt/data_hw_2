list1 = input("Enter 3 numbers:").split()
list2 = input("Enter 3 more numebrs:").split()

len1 = len(list1)
len2  = len(list2)

minlen = min(len1, len2)

final_list = []

for i in range (minlen):
    final_list.append(list1[i])
    final_list.append(list2[i])

if len1 > len2:
        final_list.extend(list1[minlen])
elif len2 < len1:
        final_list.append(list2[minlen])

print (final_list)
