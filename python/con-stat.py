age=21

if(age>=18):
    print("eligible to get married")
else:
    print("not eligible")

#2---

light="green" 

if(light=="red"):
    print("stop")
elif(light=="yellow"):
    print("get ready")
elif(light=="green"):
    print("go")
else:
    print("light is broken")

print("end of program")

#3---

num=5
if(num>2):
    print("greater than 2")
if(num>3):
    print("greater than 3")

# #IMP--DONE AND DUSTED

marks= int(input("enter your marks:"))
if(marks>=90 and marks<=100):
     grade="A"
elif(marks>=80 and marks<90):
    grade="B"
elif(marks>=70 and marks<80):
    grade="C"
else:
    grade="D"
print("grade of the student--",grade)