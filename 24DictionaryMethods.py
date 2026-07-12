# Dictionary Methods:

#1) Dict.keys():Returns all keys
#eg:

Course={
    "Faculty":"Bce",
    "Semester":6,
    "Marks":{
        "phy":97,
        "DSA":96,
        "Java":87
    }
}
print(Course.keys())#op:(['Faculty', 'Semester', 'Marks'])

#Note:we can also print the length of dictionary
print(len(Course)) #op:3

#Note: we can also typecast the dictionary
print(list(Course.keys())) #['Faculty', 'Semester', 'Marks']


#2)Dict.values():returns all values

college={
    "Faculty":"Bce",
    "Semester":6,
    "Marks":{
        "phy":97,
        "DSA":96,
        "Java":87
    }
}
print(college.values())#op:(['Bce', 6, {'phy': 97, 'DSA': 96, 'Java': 87}])

#3)Dict.items():returns an (key,value)pairs as tuples

print(college.items())#([('Faculty', 'Bce'), ('Semester', 6), ('Marks', {'phy': 97, 'DSA': 96, 'Java': 87})])

#4)Dict.get():returns the key according to value
#eg
college={
    "Faculty":"Bce",
    "Semester":6,
    "Marks":{
        "phy":97,
        "DSA":96,
        "Java":87
    }
}
print(college.get("Faculty"))#Bce:op

#5)Dict.update():inserts the specified items to dictionary

college={
    "Faculty":"Bce",
    "Semester":6,
    "Marks":{
        "phy":97,
        "DSA":96,
        "Java":87
    }
}
college.update({"address":"janakpurdham"})#update value in dictionary
print(college)
#op:{'Faculty': 'Bce', 'Semester': 6, 'Marks': {'phy': 97, 'DSA': 96, 'Java': 87}, 'address': 'janakpurdham'}