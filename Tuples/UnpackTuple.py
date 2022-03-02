# If the number of variables is less than the number of values, you can add an * to variable name and the values will be assigned to the variable as a list:
lang = ("Python", "C", "C++", "Assembly")
(high, *mid, low) = lang # unpacking the tuples into variables
print(high)
print(mid)
print(low)
