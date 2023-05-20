#6. Different built-in methods on set - there are various method available for set that are used to perform mathematical set operation.
 
#1). union() - it return the combined set of two set, containing elements of both set together.
# it can also be done using "|" operator
''' Syntax:  set_name1.union(set_name2)
                  set_name1 | set_name2   '''
set1={2,4,6,8,10}
set2={"a","e","i","o","u"}
set3={0b101,0o45,0xAE,2.3-5j}
print(set1.union(set2))
print(set1.union(set3))
print(set1 | set2)
print(set1 | set2 | set3)
print(set1.union(set2.union(set3)))

# assigning to variable
a=set2.union(set3)
print(a)
set4={"@","#","$","&"}
b=set1 | set4
print(b)
print(a | b)

# using set as argument 
print({2,4,6,8,10}.union({"a","e","i","o","u"}))
print({1,2} | {3,4})
