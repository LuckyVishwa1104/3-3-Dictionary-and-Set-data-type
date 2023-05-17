#10. all() - return true value when all elem. are true or set is empty else return false value.
# Syntax:   all(set_name)
set1={2,4,6,8,10}
print(all(set1))
set2={"a","e","i","o","u"}
print(all(set2))
# assigning to variable
set3={True and True,"fall",False or True,8,9-7j}
a=all(set3)
print(a)
#for empty set it will return True value
set4={}
b=all(set4)
print(b)
# using set as argument.
print(all({66,955.8,0,False,bool(0)}))
# conditions for list all()
# True , True = True
# True , False / False , True = False
# False , False = False
# empty list = True