#8). isdisjoint() - this method return True if sets are disjoint(no common elements) else return false.

#Syntax:  set1.isdisjoint(set2)
set1={2,4,6,8}
set2={10,12}
set3={"a","e","i","o","u"}
set4={"b","d","s","k"}
print(set1.isdisjoint(set2))
print(set3.isdisjoint(set4))

# assigning to variable
a=set4.isdisjoint(set3)
print(a)

# it also takes iterables as parameter, iterables are converted to set and then operation is performed.
b=set3.isdisjoint(["a","b","c","d"])
print(b)
print(set2.isdisjoint((14,15)))

# using set as argument
c={1,2,3}.isdisjoint({4,5})
print(c)
print({""}.isdisjoint([""]))
