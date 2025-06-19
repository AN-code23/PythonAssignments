#Merge two unsorted lists into one sorted list

#Append:
list1 = [1, 7, 6, 3]
list2 = [8, 5, 6, 2]

for item in list2:
    list1.append(item)

list1.sort()

print(list1)

#extend:
list1 = [1, 7, 6, 3]
list2 = [8, 5, 6, 2]

list1.extend(list2)

list1.sort()

print(list1)




