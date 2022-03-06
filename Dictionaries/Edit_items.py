carInfo = {"model" : "Cybertruck",
           "brand" : "Tesla",
           "year-launch" : 2019,
           "Price" : "$39,900"
          }
print(carInfo)
carInfo["Price"] = "$69,900" # editing 'Price; : value 
print(carInfo)
# like this way also we can edit (given below); but key name must match, otherwise the the item gets added
carInfo.update({"year-launch" : 2021})
print(carInfo)

# OUTPUT: 
# {'model': 'Cybertruck', 'brand': 'Tesla', 'year-launch': 2019, 'Price': '$39,900'}
# {'model': 'Cybertruck', 'brand': 'Tesla', 'year-launch': 2019, 'Price': '$69,900'}
# {'model': 'Cybertruck', 'brand': 'Tesla', 'year-launch': 2021, 'Price': '$69,900'}