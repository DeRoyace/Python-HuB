# A Dictionary is a collection of key: value pairs 
# It is ordered, i.e can be access by index 
# It can also be modified 
# Duplicate items not allowed.
wiki = {"Python" : "It is a high-level, intepreted object-oriented programming language.",
        "Google" : "A search engine",
        "Github" : "GitHub is a web-based version control repository on the Internet with a hosting service.",
        "Linux"  : "An open-source unix like OS based on  Kernel"
        }
print(wiki.items()) # returns list of tupples
print(wiki.keys()) # returns the list of keys present in dictionary
print(wiki["Github"]) # prints the value of key
print(wiki.get("Google")) # same as above statement
print() # giving a line gap

mix = {'Apple'  : "a fruit",
       'Potato' : "A vegetable",
       'numbers': [1, 2, 3, 4, 5, 6, 7, 8, 9],
       'month'  : "March",
       'year'   : 2022
      }
print(mix) # prints the whole dictionary
print(len(mix)) # returns the size of dictionay (i.e., number of keys)
print(type(mix)) # prints the type of variable mix

# OUTPUTS: 
# dict_items([('Python', 'It is a high-level, intepreted object-oriented programming language.'), ('Google', 'A search engine'), ('Github', 'GitHub is a web-based version control repository on the Internet with a hosting service.'), ('Linux', 'An open-source unix like OS based on  Kernel')])
# dict_keys(['Python', 'Google', 'Github', 'Linux'])
# GitHub is a web-based version control repository on the Internet with a hosting service.
# A search engine

# {'Apple': 'a fruit', 'Potato': 'A vegetable', 'numbers': [1, 2, 3, 4, 5, 6, 7, 8, 9], 'month': 'March', 'year': 2022}
# 5
# <class 'dict'>