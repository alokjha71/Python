"""
SET in python:Set is the collection of unordered items
=>Each element in the set must be unique and immutuable(unchangeable)

note:we can print string,float,int,tuple inside set
note:we can not create list,dictionary inside set


"""

#nt:In case of multiple duplicate values, set will ignore duplicate values
#eg.set

collection={1,2,2,3,4,"hello","world","Alok"}

print(collection)#op:{1, 2, 3, 4, 'hello', 'Alok', 'world'}
print(type(collection)) #op:<class 'set'>
print(len(collection)) #op:7(nt:duplicate values will be ignored)

#to create empty set:
#eg

collection=set()

print(type(collection)) #op:<class 'set'>