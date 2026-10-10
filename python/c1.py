#typecasting
x = 323
print(type(x))

x=18
print(x >=100)

#string

first = "Hello"
second = "World"

result = first + second

print(result)

#string printing multiple times

name="sachin"
print(name * 1)

#string indexing and slicing

name = "PYTHON"
print(name[0])
print(name[2])
print(name[-2])
print(name[3:1:4])
print(name[0:6:2])
print(name[0:4])

# reverse a string

name = "PYTHON"
print(name[::-1])

# capitalize

s= "hello world"
print(s.capitalize())

# upper
print(s.upper())

# lower
print(s.lower())

# swapcase
print(s.swapcase())

# title
print(s.title())

# split
print(s.split())

# join
s1 = "Hello"   
s2 = "World"
s3= "Python"
s4= "Programming"
result = " ".join([s1, s2, s3, s4])
print(result)

#find
s = "learning python is very easy"
print(s.find("python"))
print(s.find("java"))

#replace
s = "learning python is very easy"
print(s.replace("python", "java"))