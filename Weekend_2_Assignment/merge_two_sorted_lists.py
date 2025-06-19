# Merge two sorted lists into one sorted list

#extend:
list1= [1,3,5,7]
list2= [2,4,6,8]

list1.extend(list2)

list1.sort()

print(list1)

#Append:
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]

for item in list2:
    list1.append(item)

list1.sort()

print(list1)


