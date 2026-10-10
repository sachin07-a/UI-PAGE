#FUNCTIONS

# 1.SUM OF TWO NUMBERS

def calc_sum(a,b): #function defination,parameters
    sum=a+b
    print(sum)
    return sum

calc_sum(1,34)  #function call,arguements
a=3
b=4

#METHOD---2

def calc_sum(a,b):
    return a+b

sum=calc_sum(1,2)
print(sum)


# 2.average of three numbers    
def calc_avg(a,b,c):
    sum=a+b+c
    avg=sum/3
    print(avg)
    return(avg)
calc_avg(1,1,6)

#--TYPES OF FUNCTIONS--

# A.built in (print(),len(),type(),range())
# B.user defined

print("nyc","dsu")
print("nyc",end=" ")
print("dsu")

# 3.product of two numbers

def prod_num(a,b):
    print(a*b)
    return(a*b)
prod_num(5,8)

#q1---

cities=["pune","delhi","coorg","manali"]

def print_len(list):
    print(len(list))

def print_len(list):
    for item in list:
        print(item, end="")

print(cities)

#q2---
def calc_fact(n):
    fact=1
    for i in range(1,n+1):
        fact *=i
    print(fact)
calc_fact(5)

#Q3---

def converter(usd_val):
    inr_val=usd_val*93
    print(usd_val,"USD=",inr_val,"INR")
converter(2000)

