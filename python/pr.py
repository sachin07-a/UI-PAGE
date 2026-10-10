i = 1
while i < 6:
    print(i)
    i += 1   # increment — without this, the loop runs forever  

# break — exit immediately
n = 0
while True:
    n += 1
    if n == 5:
        break          # loop stops at 5, no matter what
print(n)  # 5

#CODE FOR PRINTING ODD NUMMBERS FROM 1-10
# continue — skip to next iteration
n = 0
while n < 10:
    n += 1
    if n % 2 == 0:
        continue       # skip the print for even numbers
    print(n) 

# No break → else runs
i = 0
while i < 3:
    print(i)
    i += 1
else:
    print("Loop completed normally")  # ✅ This prints     

# break fires → else is skipped
i = 0
while i < 3:
    if i == 2:
        break
    print(i)
    i += 1
else:
    print("Loop completed normally")  # ❌ Never prints  


target = 7
i = 0
while i < 10:
    if i == target:
        print(f"Found {target} at index {i}")
        break
    i += 1
else:
    print(f"{target} not found in range")  # only if we never broke    
