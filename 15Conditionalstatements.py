# Conditionals statements

#1: If-elif-else
#eg:Traffic light system  program

light="yellow"

if(light == "green"):
       print("Go")
elif(light == "Red"):
  print("stop")
elif(light == "orange"):
    print("wait")
else:
    print(" Traffic light is broken")

# 2)example prgram using if-else

age=5

if(age>=16):
    print("can  vote ")
    print("can drive")
else:
    print("can not vote ")

# 3)Grade students based on marks program

marks=float(input("Enter the marks of students:"))

if(marks>=90):
    print("Grade A")
elif(marks<90 and marks >=80):
    print("Grade B")
elif(marks<80 and marks >=70):
    print("Grade C")
elif(marks >70):
    print("Grade D")
else:
    print("fail")