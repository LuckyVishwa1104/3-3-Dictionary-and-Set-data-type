#5). copy() - it create and return the shallow copy of set.
#Syntax:  set_name.copy()
set1={2,4,6,8,10}
set2={4,6,8,"o","u"}
print(set1.copy())
print(set2.copy())
# assigning to variable
set3={0b101,0o45,"o","u"}
a=set3.copy()
print(a)
b=(set1^set2).copy()
print(b)
# using set as argument.
print({"",None}.copy())
