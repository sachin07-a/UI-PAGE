#LIST

marks = [90, 80, 70, 60, 50]
print(marks[0])  # Output: 90
print(marks[1])  # Output: 80
print(marks[2])  # Output: 70
print(marks[3])  # Output: 60
print(marks[4])  # Output: 50
print(type(marks))  # Output: <class 'list'>

students = ["Alice",99, 17, "Delhi"]
print(students) 
students[1] = 100  # Modifying the second element
print(students)  # Output: ['Alice', 100, 17, 'Delhi']


   #Note: strings are immutable but list is mutable 

#LIST SLICING
marks = [90, 80, 70, 60, 50]
print(marks[1:4])  # Output: [80, 70, 60]
print(marks[:3])   # Output: [90, 80, 70]
print(marks[2:5])  # Output: [70, 60, 50]
print(marks[::2])  # Output: [90, 70, 50]
print(marks[::-1]) # Output: [50, 60, 70, 80, 90]


#LIST METHODS
# 1.append a list
marks = [2, 1, 3]

marks.append(4)
print(marks)  # Output: [2, 1, 3, 4]


# 2.sort a list
marks= marks.sort()
print(marks.sort())  # Output: [1, 2, 3, 4]
print(marks)  # Output: None (because sort() returns None)  
print(marks.sort(reverse=True))  # Output: [4, 3, 2, 1] (marks is now sorted)

fruits = ["apple", "banana", "cherry"]
print(fruits.sort())  # Output: None
print(fruits)  # Output: ['apple', 'banana', 'cherry']

print(fruits.sort(reverse=True))  # Output: None
print(fruits)  # Output: ['cherry', 'banana', 'apple'] (because fruits is now sorted in reverse order)


# 3.reverse a list
list1 = [1, 2, 3]
list.reverse(list1)
print(list1)  # Output: [3, 2, 1]

# 4.insert a list
list1 = [1, 2, 3]
list1.insert(1, 4)  # Insert 4 at index 1
print(list1)  # Output: [1, 4, 2, 3]

# 5.remove a list
list1 = [1, 2, 3, 4]
list1.remove(2)  # Remove the first occurrence of 2
print(list1)  # Output: [1, 3, 4]

# 6.pop a list
list1 = [1, 2, 3, 4]
popped_element = list1.pop()  # Remove and return the last element
print(popped_element)  # Output: 4
print(list1)  # Output: [1, 2, 3]


 
