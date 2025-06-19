#Demonstrate set operations: union, intersection, difference
#Hint :  use set methods provided by python

#Method 1:
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("Union:", set1 | set2)          # Union with | operator
print("Intersection:", set1 & set2)   # Intersection with & operator
print("Difference:", set1 - set2)     # Difference with - operator

#Method 2:
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union: all elements from both sets, no duplicates
union_set = set1.union(set2)
print("Union:", union_set)

# Intersection: elements common to both sets
intersection_set = set1.intersection(set2)
print("Intersection:", intersection_set)

# Difference: elements in set1 but not in set2
difference_set = set1.difference(set2)
print("Difference:", difference_set)


