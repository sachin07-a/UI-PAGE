#TUPLE : a built-in data structure in Python that is used to store an ordered collection of items.
#  Tuples are similar to lists, but they are immutable, meaning that once a tuple is created, 
# its elements cannot be changed, added, or removed. 
# Tuples are defined by enclosing the elements in parentheses () and separating them with commas.

tup = (1, 2, 3, 4, 5)
print(tup)  # Output: (1, 2, 3, 4, 5)   
print(tup[0])  # Output: 1
print(tup[1])  # Output: 2
print(type(tup))  # Output: <class 'tuple'>

print(tup[1:4])  # Output: (2, 3, 4)

#tuple methods

# 1.index method

tup = (1, 2, 3, 4, 5)
print(tup.index(3))  # Output: 2 (the index of the first occurrence of 3)
print(tup.index(5))  # Output: 4 (the index of the first occurrence of 5)
print(tup.index(1))  # Output: 0 (the index of the first occurrence of 1)

# 2.count method
tup = (1, 2, 3, 4, 5, 3, 2, 1)
print(tup.count(3))  # Output: 2 (the number of occurrences of 3)
print(tup.count(2))  # Output: 2 (the number of occurrences of 2)
print(tup.count(1))  # Output: 2 (the number of occurrences of 1)
