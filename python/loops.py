#LOOPS--used to repeat instructions

# a. While-loop

count=1
while count<=5:
    print("hello")
    count +=1
    print("END")

i=1 #iterator--
while i<=5:
    print("nyc", i)
    i+=1 # increment/decrement

i=3 #iterator--
while i<7:
    print("nyc", i)
    i-=1
    break


#q1--PRINT NUMBERS FROM 1--100

i=1
while i<=100: #stopping condition 
    print(i,i*i)
    i+=1

#q2--print numbers from 100 to 1 in reverse order

i=100
while i>=1:
    print(i)
    i-=1

#q3---prinnt the multiplication table of a number

n=int(input("enter your number:"))
i=1
while i<=10:
    print(n*i)
    i+=1

#q4--print the following list using a loop [1,4,9,16,25,36,49,64,81,100]

nums =[1,4,9,16,25,36,49,64,81,100]

idx=0
while idx < len(nums):
    print(nums[idx])
    idx+=1

num=(1,4,9,16,25,36,49,64,81,100)

x=36
i=0 #initialization

while i<len(num):
    if(num[i]==x):
        print("FOUND at idx",i)
    else:
        print("finding---")
    i+=1