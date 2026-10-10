#--RECURSION--when a function call itself repeatedly

def show(n):
    if(n==0): #base case--IF NOT USED CODE RUNS INFINITELY
        return
    print(n)
    show(n-1)
    print("END")
show(3)

def show(n):
    if(n==-1): #base case
        return
    print(n)
    show(n-1)
show(5)


def fact(n):
    if(n==0 or n==1):
        return 1
    return n*fact(n-1)
print(fact(5))


#q1---sum of  first n-natural nummbers


def calc_sum(n):
    if(n==0):
        return 0
    return calc_sum(n-1)+n

sum = calc_sum(3)
print(sum)