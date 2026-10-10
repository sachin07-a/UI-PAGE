# q1---
#print the elements of the following list using loops--[1,4,9,16,25,36,49,64,81,100]


sq=[1,4,9,16,25,36,49,64,81,100]

for val in sq:
    print(val)


# q2---
#search for a number x in this tuple using loop---[1,4,9,16,25,36,49,64,81,100]

sqr=[1,4,9,16,25,36,49,64,81,100]
x=49

idx=0
for val in sqr:
    if(val==49):
        print("val found at idx", idx)
    idx +=1 
