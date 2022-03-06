dict = {"VSC" : "Visual Studio Code",
        "CLA" : "Command Line Arguments",
        "VR"  : "Virtual Reality",
        "DSA" : "Data Structures and Algorithms",
        "DBMS": "Data-Base Management System"
        }
print("Dictionary Keys are:")
for x in dict:   # we also do => for x in dict.keys():
    print(x) # prints the keys of the dictionary

print("------------------------------------------------------")
print("Dictionary Values are:")
for x in dict:   # we also do => for x in dict.values():
    print(dict[x]) # prints the values of the dictionary

print("------------------------------------------------------")
print("Keys         Values")
for key, value in dict.items():
    print(key, " = ", value) # prints the keys and their corresponding values.

# OUTPUT: 
# Dictionary Keys are:
# VSC
# CLA
# VR
# DSA
# DBMS
# ------------------------------------------------------
# Dictionary Values are:
# Visual Studio Code
# Command Line Arguments
# Virtual Reality
# Data Structures and Algorithms
# Data-Base Management System
# ------------------------------------------------------
# Keys         Values
# VSC  =  Visual Studio Code
# CLA  =  Command Line Arguments
# VR  =  Virtual Reality
# DSA  =  Data Structures and Algorithms
# DBMS  =  Data-Base Management System