mySet = {"Maths", "Physics", "Computer Science"}
print(mySet)
mySet.add("Statistics") # sets are unordered so it can add items at any position
print(mySet)
mySet.update("ENVS") # each letters inserts in set at any position
print(mySet)

set2 = {"History", "Geography"}
print(set2)
set2.update(mySet) # set2 gets updated with items from 'mySet'
print(set2)

# OUTPUT: 
# {'Computer Science', 'Maths', 'Physics'}
# {'Computer Science', 'Maths', 'Physics', 'Statistics'}
# {'Computer Science', 'V', 'Maths', 'E', 'Physics', 'Statistics', 'N', 'S'}
# {'Geography', 'History'}
# {'Computer Science', 'V', 'Maths', 'E', 'Physics', 'Statistics', 'History', 'Geography', 'N', 'S'}