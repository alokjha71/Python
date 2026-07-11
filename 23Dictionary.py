""" 
Dictionary in python:Dictionaries are used to store data values in key:valuepairs
They are unordered ,mutuable(changrable),and don't allow duplicate keys

note;we can add different data types in dictionary

"""

#eg.1
dict={
    "key":"Value",
    "name":"Alok",
    "address":"Janakpurdham",
    "Degree":"Engineering"
}
print(type(dict)) #op:<dict>
print(dict)

#nt:we can also access particular key from dictionary

print(dict["name"]) #op:Alok
print(dict["Degree"]) #op:Engineering

#nt:we can also change values of key [key:value]

dict["name"]="Gungun"
print(dict) 

#nt:We can also assign new keys in dict

dict["surname"]="jha"
print(dict)


# Nested Dictionary
#eg:

student={
    "name":"Alok",
    "subjects":{
        "phy":98,
        "che":97,
        "math":99
    },
"address":"jnk"

}
print(student)
print(student["subjects"]) #op:'phy':98,'che':97,'mth':99
print(student["subjects"]["che"]) #op:'che':97

