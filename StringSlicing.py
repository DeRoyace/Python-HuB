# String Slicing means getting the sub-part/ portion of a string.  
str =  "De Royace"
#Index: 012345678
#  -9, -8, -7, -6, -5, -4, -3, -2, -1 => Negative indexes [ -1 starts from 'e' -> pos 8]
print(str[3])
print(str[3 : 6]) # printing string characters from index 3 to 5
print(str[6:]) # prints all characters from index 6 to end
print(str[:6]) # prints all characters before index 6 [index: 0 to 5]
print(str[-6:]) # prints characters from index (-ve) 6 [ index: -6 to -1]
print()

# now we see how to Skip value/ character(s) while Slicing the string:
str = "Switzerland"
print(str[0:11:1]) # we can't see any change
# [start_index : end_index : N-valuestoskip]
# so the value we give for skip string characters asct as N-1 characters skipped
print(str[0:11:2]) # N = 2; so we are skipping 1 character while slicing the string
print(str[0::3]) # slicing from 0 to end; here N =2; so we are skipping 2 characters.