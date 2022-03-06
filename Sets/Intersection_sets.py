set1 = {17, 65, 89, 100}
set2 = {45, 89, 97, 123}
print(set1.intersection(set2)) # prints the common elements between two sets
print(set1.symmetric_difference(set2)) # prints the non-common elements of two sets
print("set1 =",set1, ";  set2 =", set2)
set1.symmetric_difference_update(set2) # set1 = set1 + set2; provided it excludes common items
print(set1)