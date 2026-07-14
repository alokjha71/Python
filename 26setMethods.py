#Set Methods in python:
#1)set.add(el)
#nt:we can add strings,numbers ,tuple etc in set but not list,dictionary

#eg

collection=set()

collection.add(1)
collection.add(2)
collection.add("Hello")
collection.add((1,2,3))#Tuple
print(collection)#op:{1, 2, (1, 2, 3), 'Hello'}

#2)set.remove()=>removes the elements

course=set()

course.add("DSA")
course.add("Python")
course.add("java")

course.remove("java")#removes java from set
print(course)#{'DSA', 'Python'}

#3)set.clear()=>clears the set

Book=set()

Book.add("Math")
Book.add("Python")

Book.clear() #clear the set
print(Book) #set()

#4)set.pop()=>removes random values

collection={"course","python","AI"}

print(collection.pop())#AI
print(collection.pop())#Python
