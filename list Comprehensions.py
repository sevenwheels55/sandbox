# Make a new list with even numbers only from list a
"""
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = [even for even in a if even % 2 == 0]

print(b)
"""

# This will make a list of 9 items
"""
x = [1, 2, 3]
y = [5, 10, 15]
allproducts = [a*b for a in x for b in y]
"""

# This will add all the odd list numbers to a new list

'''
x = [1, 2, 3]
y = [5, 10, 15]
customlist = [a*b for a in x for b in y if a*b%2 != 0]

print(customlist)
'''

# this list comprehension will create a list with items shared by two lists and disregards doubles
"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = [i for i in set(a) if i in b]
print(c)
"""