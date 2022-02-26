str = "Learning Python Strings"
#Index 0123456789...
print("String lenth is ", len(str))

print(str.index("P")) # prints the index of 'P'
print(str.index("Str")) # prints the starting index of the given string if present in str
# print(str.index("hello")) # throws error

print(str.replace("Py", "Jy")) # replacing the strings
print(str) # we can't see the affect of replace function
str = str.replace("Py", "Cy") # replacing the strings and making the changes in original string
print(str) # now we can see the affect of replace function

print("Is the string in Uppper case? ", str.isupper())
str = str.upper() # converts string to upper case
print("New Case: " + str)