arr = (10, 20 , 30, 40 ,50, "Sixty", 70.0, 'Eighty', '''90''', "Hundred")
print("arr =",arr)
brr = arr # tuple arr is copied to brr
print("brr =", brr)
crr = arr[:] # another way to copy tuple
print("crr =", crr)

# OUTPUT:
# arr = (10, 20, 30, 40, 50, 'Sixty', 70.0, 'Eighty', '90', 'Hundred')
# brr = (10, 20, 30, 40, 50, 'Sixty', 70.0, 'Eighty', '90', 'Hundred')
# crr = (10, 20, 30, 40, 50, 'Sixty', 70.0, 'Eighty', '90', 'Hundred')