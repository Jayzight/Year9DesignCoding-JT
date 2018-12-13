odd = [1, 3, 5]

#We can add one item to a list using append() method or add several items 
#using extend() method.
print(odd)
odd.append(input("Add Number:"))

# Output: [1, 3, 5, 7]
print(odd)

###################

# Furthermore, we can insert one item at a desired location by using the 
#method insert() or insert multiple items by squeezing it into an empty 
#slice of a list.

odd.extend(input("Add Numbers:"))

# Output: [1, 3, 5, 7, 9, 11, 13]
print(odd)

