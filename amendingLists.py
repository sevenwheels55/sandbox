"""Find the number in the list that are lower than 5."""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
newlist = []
for item in a:
    if item < 5:
        newlist.append(item)

print(newlist)

"""check to see if there are duplicates in list a and b and print them out"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c =[]

for i in a:
    if i in b:
        """If the number isn't in list c already then go ahead and append it."""
        if not i in c:
            c.append(i)

print(c)

"""Like the sequence above but with randomly generated lists."""

import random

d = []
e = []
f = []

lowerLimit = 0
upperLimit = 100
randomLength = random.randint(lowerLimit, upperLimit)

for i in range(randomLength):
    d.append(random.randint(lowerLimit, upperLimit))
for j in range(randomLength):
    e.append(random.randint(lowerLimit, upperLimit))

for k in d:
    if k in e:
        if not k in f:
            f.append(k)

print(f)