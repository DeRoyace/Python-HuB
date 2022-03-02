# A tuple is alse a collection of datas/ objects/ items that can be of same type or different; just like a list
# Points to NOTE: 
#   tuples are ordered i.e indexed position wise 
#   tuples are unchangeable/ immutable - i.e, we can't add or delete items 
#   tuple allows duplicate elements.

# the tuple below is storing numbers 
point = (7, 9)
print(point)
print(point[1]) # we can access tuple elemnents by their index.

axb = [(1,2), (1,3), (2,3)] # tuples inside a list
axb[1] = (4,5) # changing list tuple
print(axb)