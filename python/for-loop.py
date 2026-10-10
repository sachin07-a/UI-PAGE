#FOR--LOOP
#for loops are used for sequential traversal in list,string,tuples..

# 1.
veggies=["potato","tomato","brinjal","lady-finger","cucumber"]

for val in veggies:
    print(val)

# 2.

tup= (1,2,3,4,5,6)

for val in tup:
    print(val)

# 3.

str="nyc"

for char in str:
    print(char)
else:
    print("END")

# 4.

str="nyc"

for char in str:
    if (char=='y'):
        print('y found')
        break
    print(char)
else:
    print("END")

