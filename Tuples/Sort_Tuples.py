arr = (89, 77, 90, 81, 100, 99, 97, 85)
brr = sorted(arr) # sorting the list brr
print("brr =", brr, type(brr))
crr = tuple(brr) # converting list into a tuple
print("crr =", crr, type(crr))

# OUTPUT:
# brr = [77, 81, 85, 89, 90, 97, 99, 100] <class 'list'>
# crr = (77, 81, 85, 89, 90, 97, 99, 100) <class 'tuple'>