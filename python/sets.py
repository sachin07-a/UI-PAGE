#SETS--  collection of unordered items and each collection in the set should be immutable and unique
#we cant store list and dictionnaries in stes because they mutable 

collection = {1,2,3,4,5,"hello"}


#repeating elements in the sets are ignored

print(collection)
print(len(collection))

# pot = {} , is not a set its an dictionary
pot = set() #THE WAY TO WRITE A EMPTY SET

#SET METHODS

# 1.ADD

val= set()
val.add(1)
val.add("apna college")
val.add((2,3,4,5,6)) #no error
# val.add([2,3,4,5,6]) # error

print(collection)

# 2.remove

val.remove(1)

# 3.clear

val.clear()
print(len(val))

# 4.pop

coll = {"hello","hi","rakshita","java"}
print(coll.pop())


#SET--METHODS

# A.UNION
set1= {1,3,2}
set2= {3,4,5}
print(set1.union(set2))
print(set1.intersection(set2))

