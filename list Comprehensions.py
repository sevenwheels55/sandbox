# Make a new list with even numbers only from list a

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = [even for even in a if even % 2 == 0]

print(b)