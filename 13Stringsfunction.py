# Strings function

#a)str.ends with(" "):return true if string ends with substrings

str="I believe in god"
print(str.endswith("od")) #True output

#b)str.capitalize():capatilizes first char

str1="god is all around the world"
print(str1.capitalize()) #output:God is all around the world

#c)str.replace(old,new):replaces old value with new

str="I am learning python "
print(str.replace("a","b"))
print(str.replace("python","cybersecurity"))#output:I am learning cybersecurity

#d)str.find(word)#search for word in string and returns index of that word where itcomes first

str="I believe in hardwork "
print(str.find("i")) #op:5

#e)str.count("word"):counts the occurance of substring in our string

str="I am from janakpurdham.\n.I came from jnk to kathmandu to fulfill my dreams of mine and my parents.\n.I will achieve all my dreams"
print(str.count("from"))

