# This list given below is storing names of several countries 
country = ["USA", "Australia", "India", "Japan", "New Zealand", "Germany", "France", "Russia"]
# Index :    0         1          2        3           4            5          6         7
# (-ve) :   -8        -7         -6       -5          -4           -3         -2        -1

country[0] = "America" # changing the list value of a specified index
print(country)
country[4:6] = ["Italy", "Spain", "Belgium"] # like this we can change and insert elements
print(country)

item = ["PEN", "PENCIL", "ERASER", "SHARPNER", "SCALE"]
item[2:5] = ["RULER"] # changing last 3 items and replacing them by one.
print(item)