# Practice Questions:
""" 
1)WAP to ask the user to enter names of their  3 favourite 
 movies and store them in a list

"""
 
movies=[]

mov1=input("Enter the name of first flim:")
mov2=input("Enter the name of second movie:")
mov3=input("Enter the name of third movie:")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies) #op:["xtz","abc","aaa"]

"""
2) WAP to check if a given list contains a palindrome of 
 elements 
"""
list1=[1,2,1]

copy_list1=list1.copy()
copy_list1.reverse()

if(copy_list1==list1):
    print("Palindrome")
else:
    print("Not a Palindrome")


"""
3) WAP to count the number of students with the grade "A" in following
tuple
"""

grade=("C","A","A","B","C","E","A")

print(grade.count("A")) #op:3

"""
4)WAP to sort the list from A to Z
 list=["C","A","A","B","C","E","A"]
"""
list=["C","A","A","B","C","E","A"]
list.sort()
print(list)