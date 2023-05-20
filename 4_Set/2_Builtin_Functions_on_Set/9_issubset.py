#9). issubset() - this method return True if one set is subset of other, else return False.

#Syntax:  set1.issubset(set2)
set1={2,4,6,8}
set2={4,8}
set3={"a","e","i","o","u"}
set4={"i","o","u"}
print(set2.issubset(set1))
print(set4.issubset(set3))

# assigning to variables
a=set2.issubset(set3)
print(a)

# it also takes iterables as parameter, iterables are converted to set and then operation is performed.
b=set2.issubset([2,4,6,8,10])
print(b)
print(set4.issubset({"a":1,"e":2,"i":3,"o":4,"u":5 }))

# using set as argument
print({22,33,44}.issubset({22,55,66}))
print({""}.issubset({""})) 