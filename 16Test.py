# WAP to check if the given number entered by user is even or odd

num=int(input("Enter the number:"))

if(num%2==0):
    print(" Number is even")
else:
    print("Number is  odd number")


#WAP to find greatest of 3 numbers entered by the user

a=int(input("Enter first number a:"))
b=int(input("Enter second number b:"))
c=int(input("Enter third number c:"))

if(a>=b and a>=c):
        print("a is greateest")
elif(b>=c):
    print("b is greatest")
