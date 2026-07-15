"""
Q.1)Store the following word meanings in a python dictionary
   table:"a piece of furniture","list of facts and figures"
   cat:"a small animal"
"""

dict= {
    "cat":"a small animal",
    "table":["a piece of furniture","list of facts and figures"]
}
print(dict)

"""
Q.2)You are given a list of subjects for stidents.
Assume one classroom required for 1 subject.
How many classrooms are needed by all the students
"""

subjects={
"python","java","c++",
"python","Javascript","java","python","java","c++","c"}

print(len(subjects))#op:5

"""
Q.3)WAP to enter the marks of 3 students from the user and store them
in a dictionary.start with an empty dictionary and add one by
one.use subjects name as a key and marks as a value
"""
marks={}


x=int(input("Enter marks of physics:"))
marks.update({"physics":x})

y=int(input("Enter marks of chemistry:"))
marks.update({"chemistry":y})

p=int(input("Enter marks of Python:"))
marks.update({"Python":p})

print(marks)#op:{'physics': 98, 'chemistry': 97, 'Python': 96}

"""
Q.4)Figure out a way to store 9 and 9.0 as seprate values in set

"""

values={
    "9",9.0
}
print(values)