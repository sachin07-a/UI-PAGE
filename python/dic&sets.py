#DICTIONARY: are used to store data in key value pairs
#Dictionaries are mutable, meaning that you can change their content without changing their identity.

info={
    "key" : "value",

    "name" : "John",
    "age" : 30,
    "city":"pune",
    "marks":90,
    "subjects":["ieee","physics","maths"],
    "topics":("qubit","o-state","1-state")
}

print(type(info))
print(info["marks"])
print(info["name"])

#assigning new value for a particular key

info["name"] = "sachin"
print(info)

#nested dictionaries

students = {
    "name": "sachin",
    "subjects": {
        "phy":89,
        "math":91,
        "bio":99,
        "chem":85
    }
}

print(students["subjects"])
print(students["subjects"]["chem"])
print(students["subjects"]["bio"])
print(students["subjects"]["math"])

#dictionaries methods

# 1.keys

students.keys()
print(students.keys())
print(list(students.keys()))
print(len(students))

# 2.values
print(students.values())
print(list(students.values()))

# 3.items

print(students.items())
print(list(students.items()))

pairs = list(students.items())
print(pairs[0])

# 4.Get

# print(students["name2"]) --error


print(students.get("name2")) #--no error

print("BEFORE")
# print(students["name2"])
print("AFTER")

# 5.update

new_dict= {"name":"sophie" ,"age":44}
# students.update({"city": "delhi"}) or
students.update(new_dict)

print(students)





