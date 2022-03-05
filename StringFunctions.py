from cupshelpers import Printer


str1 = "Learning Python Strings"
#Index 0123456789...
print("String lenth is ", len(str1))
print("Occurence of 'n' :", str1.count("n")) # prints the no. of occurence of 'n;

print(str1.index("P")) # prints the index of 'P'
print(str1.index("Str")) # prints the starting index of the given string if present in str
# print(str.index("hello")) # throws error

print(str1.replace("Py", "Jy")) # replacing the strings
print(str1) # we can't see the affect of replace function
str1 = str1.replace("Py", "Cy") # replacing the strings and making the changes in original string
print(str1) # now we can see the affect of replace function

str2 = "Lime soda drink"
print("Is the string in Uppper case? ", str2.isupper())
str2 = str2.upper() # converts string to upper case
# Similarly, we can use islower() to check all characters in strings are lower or not
# And lower() to make all characters of the string to lower case.
print("New Case: " + str2)

str3 = "   There are white    spaces at front and end    "
print(str3)
print(str3.strip()) # strip removes white spaces from both sides of the string

str4 = "coding is the new bing!"
str4 = str4.capitalize() # this capitalizes the first character of a string
print(str4)
print(str4.find("bing")) # prints the starting index of that word if found otherwise -1.
print(str4.endswith("!")) # returns true if the string ends with the given string.

strnum = "97"
print("Is the string contains numeric digits ONLY? ", strnum.isdigit()) # return true if the given string is a digit