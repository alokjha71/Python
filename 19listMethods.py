# List Methods:

#1)list.append()

list=[1,2,3]
list.append(4)
print(list) #op:[1,2,3,4]

#2)list.sort=>arranges list in ascending order

list=[2,3,1,4,6,8,7,9,0]
list.sort()
print(list) #[0,1,2,3,4,6,7,8,9]:output

#3)list.sort(reverse=True):sorts in descending order
# note: we can also sort strings

list=["a","b","h","e","g","k","c"]
list.sort(reverse=True)
print(list) #arranged list in descending order

#4)list.reverse()=>reverselist

list=["a","b","c","d"]
list.reverse()
print(list) #["d","c","b","a"]

#5)list.insert(idx,el): adds new  element at particular index

list=[1,2,3,4]
list.insert(2,0)
print(list)

#6) list.remove():removes first occurance of element

list=[1,2,3,4,2]
list.remove(2)
print(list)#op:[1,3,4,2]

#7) list.pop(idx):removes element at particular index

list=[2,3,4,5]
list.pop(2)
print(list) #op:[2,3,5]