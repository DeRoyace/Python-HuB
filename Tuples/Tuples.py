# A tuple is alse a collection of datas/ objects/ items that can be of same type or different; just like a list
# Points to NOTE: 
#   tuples are ordered i.e indexed position wise 
#   tuples are unchangeable/ immutable - i.e, we can't add or delete items 
#   tuple allows duplicate elements.

# the tuple below is storing numbers 
point = (7, 9)
print(point)
print(point[1]) # we can access tuple elemnents by their index.

mix = (2022, "hello", 97.89, True, [7, 9], True, 2022)
# tuples can store different data types and duplicate values. 
print(mix)
print(type(mix))
print("Index of 2022 is ", mix.index(2022)) # prints the first index

num = 9, 10, 7, 8, 2, 6, 12 # we can also create tuple like these
print(num)
print(type(num))

nil = () # an empty tuple
print(nil, type(nil))

val = (99) # this is not a tuple, it will act a integer
print(val, type(val))

val2 = (98,) # this will act as tuple
print(val2, type(val2))

arr = ([4, 3]) # this will act as list
print(arr, type(arr))

brr = ([1, 6],)  # this is a tuple
print(brr, type(brr))