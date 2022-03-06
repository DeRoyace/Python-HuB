mix = {'Apple'  : "a fruit",
       'Potato' : "A vegetable",
       'numbers': [1, 2, 3],
       'month'  : "March",
       'year'   : 2022,
       'bool'   : (True, False)
      }
print(mix)
mix.pop("year") # removes 'year' and its value from the dictionary
print(mix)
mix.popitem() # removes the last item
print(mix)
mix.clear() # makes the dictionary empty
print(mix)

del mix # deletes the entire dictionary
print(mix) # will give error because dictionary is deleted