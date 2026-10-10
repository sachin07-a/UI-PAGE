#--STRINGS--

# 1.#concatenation
str1="nyc" 
str2="dsu" 
print(str1+str2) #concatenation

str1="nyc" 
str2="dsu"
final_str= str1+str2
print(final_str) 

# 2.len()

str= "rakshita  is my first crush and she will be the last one"
print(len(str))

# 3.indexing

str="apnacollege"
print(str[0])
print(str[6])
print(str[3])
print(str[4])

string="apna bandi"
# str[3]="i" ---we cant change or adding any value for any particular index
print(str)

# 4.slicing

lol="iam sachin"
print(lol[1:3])
print(lol[1:])
print(lol[:3])
print(lol[3:4])
print(lol[2:5])
print(lol[1:len(lol)])
#positive---starting is skipped [1:3]--1
#negative---last is skipped [-3:-1]-- -1

#STRING FUNCTIONS

pop="iam A coder"
print(pop.capitalize())
print(pop.endswith("er"))
print(pop.replace("A","the"))
print(pop.find("iam"))
print(pop.count("iam"))

#q1--input users first name and print its lenngth


name=input("enter your name:")
print("length of my name is:",len(name))

#q2--occurence of a 

lop="nyc is a good platform to learn coding from scratch"
print(lop.count("a"))
