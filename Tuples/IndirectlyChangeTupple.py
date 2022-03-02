# In tuples, we cannot modify anything
# But we can convert tuple to list, then change the list, and bring back to tuple again 
items = ("pizza", "burger", "hot-dog", "fries")
temp = list(items) # copying tuple items into a list
temp[2] = "sandwich"
temp.append("coke")
temp.remove("fries")
temp.insert(0, 'sausages')
newitems = tuple(temp) # copying list items into a tuple
print(newitems)