"""
#List in python:A bulit in data type that stores set of values
                =>list can store elements of differet types(int,float,string etc)

"""
#ex(1)
marks=[100,99.8,97.6,95.7]

print(marks)
print(type(marks)) #returns type of list:list
print(len(marks)) #returns length of list

# list are mutable: things can change 
#ex:2

student=["Gungun",22,"Bce","janakpurdham"]

print(student[0])
student[0]="Alok" # Gungun is changed with Alok
print(student[0])

"""
List slicing:similar to string slicing
 syntax:list_name[starting_idx:ending_idx] (ending index is not included)
"""

marks=[98,97,95,92,91]

print(marks[0:4]) #ending index is not added
print(marks[:4]) #[0:5]
print(marks[0:]) #[0:5]

print(marks[-3:-1]) #Negative slicing in list

