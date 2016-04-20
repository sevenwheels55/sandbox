a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
newlist = []
for item in a:
    if item < 5:
        newlist.append(item)

print(newlist)