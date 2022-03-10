tree = ("Mango", "Date", "Plum", "Coconut", "Neem", "Banyan", "Pine", "Eucalyptus")
# Index    0        1       2        3         4        5        6          7
#   "     -8       -7      -6       -5        -4       -3       -2         -1
print("Length of tuple 'tree':", len(tree))
print(tree[:])
print(tree[1:5]) # prints tuple items from index 1 to 4
print(tree[3:]) # print all tuple items from index 3 to end
print(tree[:6]) # prints tuple items from index 0 to 5
print(tree[-1])
print(tree[-2:-6]) # prints empty tuple because starting index should be lesser than last index
print(tree[-6:-2]) # prints from index -6 to -3
print(tree[-3:]) # prints from index -3 to -1
print(tree[:-5]) # prints from index -8 to -6

# OUTPUT:
# Length of tuple 'tree': 8
# ('Mango', 'Date', 'Plum', 'Coconut', 'Neem', 'Banyan', 'Pine', 'Eucalyptus')
# ('Date', 'Plum', 'Coconut', 'Neem')
# ('Coconut', 'Neem', 'Banyan', 'Pine', 'Eucalyptus')
# ('Mango', 'Date', 'Plum', 'Coconut', 'Neem', 'Banyan')
# Eucalyptus
# ()
# ('Plum', 'Coconut', 'Neem', 'Banyan')
# ('Banyan', 'Pine', 'Eucalyptus')
# ('Mango', 'Date', 'Plum')