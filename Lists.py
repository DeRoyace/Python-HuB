# A list is a collection of objects/ items that can be of same type or different.
# This list given below is storing names of several countries 
country = ["USA", "Australia", "India", "Japan", "New Zealand", "Germany", "France", "Russia"]
# Index :    0         1          2        3           4            5          6         7
print(country) # prints the whole list
print(country[2]) # prints the list value at index 2
print(country[3:]) # prints the lists starting from index 1
print(country[:4]) # print the lists before index 4
print(country[5:7]) # prints the lists from index 5 to 6
country[0] = "America" # changing the list value of a specified index
print(country)

# the list given below stores different types of datas in one list
list = ["String", 97, 35.6, 2+3j, False, 'H']
print(list)