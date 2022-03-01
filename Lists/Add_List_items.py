# the list given below stores different types of datas in one list:
datas = ["String", 97, 35.6, 2+3j, True, '&']
print(datas)
datas.append(False) # adds element at the end of the list
datas.append("Python")
print(datas)
item = ["PEN", "PENCIL", "ERASER", "SHARPNER", "SCALE"]
print(item)
item.insert(2, "Box") # inserts 'Box' at index 2
print(item)

# Add or Join lists
item.extend(datas) # this extends the lists by adding or joining another list items from the end
print(item)