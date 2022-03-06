shop = {"T-shirt" : "PUMA",
        "Jeans"   : "Levis",
        "Glasses" : "Ray & Ban",
        "Shoes"   : "Nike",
        "Watch"   : "Rolex"
        }
print(shop)
shop["Shirt"] = "Lee Cooper" # adding new keys and values
print(shop)

# another way to update dictionary is by using update() method:
shop.update({"Boxers" : "Calvin Klein"})
print(shop)

# OUTPUT: 
# {'T-shirt': 'PUMA', 'Jeans': 'Levis', 'Glasses': 'Ray & Ban', 'Shoes': 'Nike', 'Watch': 'Rolex'}
# {'T-shirt': 'PUMA', 'Jeans': 'Levis', 'Glasses': 'Ray & Ban', 'Shoes': 'Nike', 'Watch': 'Rolex', 'Shirt': 'Lee Cooper'}
# {'T-shirt': 'PUMA', 'Jeans': 'Levis', 'Glasses': 'Ray & Ban', 'Shoes': 'Nike', 'Watch': 'Rolex', 'Shirt': 'Lee Cooper', 'Boxers': 'Calvin Klein'}