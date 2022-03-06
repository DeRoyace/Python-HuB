country = {"Cannada", "America", "Mexico", "Brazil", "Greenland"}


country.remove("Mexico") # if element not present then it will give error
print(country)

country.discard("America") # doesn't gives error if element not present
print(country)


oceans = {"Atlantic", 'Arctic', "Antarctic", "Indian", "Pacific"}
print(oceans)
oceans.pop() # removes any random element
print(oceans)

del oceans # deletes the entire set