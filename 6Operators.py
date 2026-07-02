 # Operators: is a symbol that performs a certain operation between operands

#1:Arithmetic operator:+,-,*,/,%,**

a=23
b=4

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)# remainder is output
print(a**b) #a^b

#2: Relational operator:==,!=,<,>,>=,<=:trurns ture or false output

a=23
b=4

print(a==b) #False
print(a!=b) #True
print(a<b) # False
print(a>b) #True
print(a<=b)# False
print(a>=b) #True

#3) Assignment operator:=,+=,-=,*=,/=,%=,**=

num=10
num +=10

print("num is:",num)


#4) Logical Operator:AND,OR,NOT
#a)NOT
a=5
b=99
print(not(a<b))

#b)AND

value1=True
value2=True

print("And operator is:",value1 and value2)

#c)OR

value1=True
value2=False

print("OR operator is:",value1 or value2)
print("OR operator is:",(a==b) or (a<b))
