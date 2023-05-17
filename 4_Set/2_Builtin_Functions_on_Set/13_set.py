# set() : it is used to create a set or it convert other data-type to set.
# Syntax :  set(iterables)
ite1=22,44,55,77,(67,86)
print(set(ite1))
ite2=["g","g",65,0b110,None]
print(set(ite2))
# assigning to variables
ite3=(67,"g",0.09,8-7j,(78))
a=set(ite3)
print(a)
ite4="hello"
b=set(ite4)
print(b)
# using set as argument
print(set({"@","#","&","*" }))
