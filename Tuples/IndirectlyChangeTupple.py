# In tuples, we cannot modify anything
# But we can convert tuple to list, then change the list, and bring back to tuple again 
items = ("pizza", "burger", "hot-dog", "fries")
print("Original:", items)
temp = list(items) # copying tuple items into a list
temp[2] = "sandwich"
temp.append("coke")
temp.remove("fries")
temp.insert(0, 'sausages')
newitems = tuple(temp) # copying list items into a tuple
print("Modified:", newitems)
print()

tup = ([9,10], [1, 2, 3], [True, False])
print("Original:", tup)
# we can modify immutable elements inside a tuple, like list 
tup[0][1] = 9
tup[1][0] = tup[1][1] = tup[1][2] = 255
tup[2][1] = True
print("Modified:", tup)

# OUTPUT:
# Original: ('pizza', 'burger', 'hot-dog', 'fries')
# Modified: ('sausages', 'pizza', 'burger', 'sandwich', 'coke')

# Original: ([9, 10], [1, 2, 3], [True, False])
# Modified: ([9, 9], [255, 255, 255], [True, True])