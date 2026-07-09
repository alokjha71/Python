# Tuples:A built in data type that lets us create immutuable sequence of codes
# tuples in written as:tup()

#eg.1

tup=(1,2,3,4)

print(type(tup))#op:tuple


#nt:we can also access elements of particular index
tup=(2,3,4,5)
print(tup[1]) # op:2

#note:we can not change values of tuple

tup=(1,4,6,8)
print(tup[1])
#tup[1]=5 #error will generate
print(tup)

#Slicing in tuples is same as of strings and list

tup=(5,6,7,8)
print(tup[1:3]) #(6,7):output

print(tup[0:]) #(5,6,7,8):output
print(tup[:3]) #(5,6,7):output