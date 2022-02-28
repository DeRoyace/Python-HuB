# A list is a collection of datas/ objects/ items that can be of same type or different.
# lists are ordered i.e indexed position wise 
# we can change list items 
# list allows duplicate elements 

# This list given below is storing names of several countries 
country = ["USA", "Australia", "India", "Japan", "New Zealand", "Germany", "France", "Russia"]
# Index :    0         1          2        3           4            5          6         7
# (-ve) :   -8        -7         -6       -5          -4           -3         -2        -1

print(country) # prints the whole list
print(country[2]) # prints the list value at index 2; like these we can access list items
print(country[3:]) # prints the lists starting from index 1
print(country[:4]) # print the lists before index 4
print(country[5:7]) # prints the lists from index 5 to 6
print(country[-6:-1]) # prints the list from negative index -6 to -2

country[0] = "America" # changing the list value of a specified index
print(country)
country[4:6] = ["Italy", "Spain", "Belgium"] # like this we can change and insert elements
print(country)
print()

# the list given below stores different types of datas in one list:
datas = ["String", 97, 35.6, 2+3j, True, '&']
print(datas)
print(len(datas)) # we can print the length of the list like this
print(type(datas)) # shows it is list type
datas.append(False) # adds element at the end of the list
datas.append("Python")
print(datas)

item = ["PEN", "PENCIL", "ERASER", "SHARPNER", "SCALE"]
item[2:5] = ["RULER"] # changing last 3 items and replacing them by one.
print(item)
item.extend(datas) # this extends the lists by adding another list items from the end
print(item)
print()

fruits = ["Apple", "Banana", "Orange", "Lemon", "Guava"]
fruits.insert(3, "Cherry") # inserts Cherry at index 3.
print(fruits)
print(fruits.index("Banana")) # gets the index of given item
fruits.clear() # delets the list items
print(fruits)
print()

food = ["Sanswich", "Pizza", "Omlette", "Juice", "Sausages", "Coffee"]
food.pop() # pops out/ removes the item from last
# we can also give indexes to remove items like food.pop(2)
print(food)
food.remove("Omlette") # removes the specified item name from the list
print(food)
print()

nums = [12, 23, 14, 56, 7, 21, 98, 11, 100]
nums.reverse() # reverses the list
print(nums)
nums.sort() # sorts the list
print(nums)
del nums # deletes the entire list
# print(nums) # gives error as the list is deleted