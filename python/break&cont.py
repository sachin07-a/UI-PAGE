#BREAK--CONTINUE

i=1
while i<=5:
    print(i)
    if(i==3):
        break
    i+=1
print("END OF LOOP")

#EX--1
num=(1,4,9,16,25,36,49,64,81,100)

x=36
i=0 #initialization

while i<len(num):
    if(num[i]==x):
        print("FOUND at idx",i)
    i+=1

#METHOD--2

num=(1,4,9,16,25,36,49,64,81,100)

x=36
i=0 #initialization

while i<len(num):
    if(num[i]==x):
        print("FOUND at idx",i)
        break
    else:
        print("finding---")
    i+=1
print("END OF LOOP")

#CONTINUE-----

#terminates execution in the current iteration and continues execution of the loop with the next iteration

i=0
while i<=5:
    if(i==3):
        i+=1
        continue
    print(i)
    i+=1


#even and odd case

i=1
while i<=10:
    if(i%2==0):
        i+=1
        continue
    print( i)
    i+=1 #prints all odd numbers


    

