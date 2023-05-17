#4). symmetric_difference() - this method return the set of elements of both the set except the common element to both sets.
# it can also be done using "^" operator.
'''Syntax: set_name1.symmetric_difference(set_name2)
 set_name1 ^ set_name2   '''
set1={2,4,6,8,10}
set2={4,6,8,"o","u"}
set3={0b101,0o45,"o","u"}
print(set1.symmetric_difference(set2))
print(set2.symmetric_difference(set3))
print(set1 ^ set2)
print(set2 ^ set3)
# assigning to variable
set4={10,"o","u",88,0.9 }
a=set2.symmetric_difference(set4)
print(a)
b=set1.symmetric_difference(set2.symmetric_difference(set3))
print(b)
c=set2 ^ set4
print(c)
d=set1 ^ set2 ^ set3
print(d)
# using set as argument
print({"@","#","$"}.symmetric_difference({"&","€","$"}))
print({"@","#","$"} ^ {"&","€","$"})