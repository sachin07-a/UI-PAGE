#range--- range functions returns a sequence of numbers,starting from 0 by default and 
# increments by 1 (by default) ,and stops before a specified number

print(range(3))

seq= range(10) #10 is stopping condition or range(stop)
for i in seq:
    print(i)

# Range(start?,stop,step?)

for i in range(2,10,2):
    print(i)

#Printing even numbers fromm 1-100

for i in range(0,101,2):
    print(i)

for i in range(100,-1,-1):
    print(i)


n = int(input("enter your number:"))
for i in range(1,11):
    print(n*i)

#PASS--STATEMENT
#pass is a null statement that does nothing ,it is used as a placeholder for future code

for i in range(5):
    pass
print("hello world")


#--sum of first n-numbers
n=3
sum=0
for i in range(1,n+1):
    sum+=i
    i+=1
print("total sum=",sum)

#--factorial


#METHOD---1
n=5
fact=1
i=1

while i<=n:
    fact*=i
    i+=1
print("factorial=",fact)


#METHOD---2
n=5
fact=1

for i in range(1,n+1):
    fact*=1

print("factorial=",fact)