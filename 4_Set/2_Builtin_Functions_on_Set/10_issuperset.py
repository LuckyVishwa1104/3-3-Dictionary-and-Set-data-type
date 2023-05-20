#10). issuperset() - this method return True if one set is superset of other else return False.

#Syntax:  set1.issuperset(set2)
set1={2,4,6,8}
set2={4,8}
set3={"a","e","i","o","u"}
set4={"i","o","u"}
print(set1.issuperset(set2))
print(set3.issuperset(set4))

# assinging to variable.
a=set2.issuperset(set1)
print(a)

# it also takes iterables as parameter, iterables are converted to set and then operation is performed.
b=set2.issuperset([4])
print(b)
print(set3.issuperset(("a","u")))

# using set as argument
c={"@","#","$"}.issuperset({"8"})
print(c)
print({""}.issuperset({""}))