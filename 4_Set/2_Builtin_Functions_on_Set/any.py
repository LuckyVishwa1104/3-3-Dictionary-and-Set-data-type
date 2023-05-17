#11. any() - return True value when any one elem. is true or False when set is empty else return False.
# Syntax:   any(set name) 
set1={2,4,6,8,10}
print(any(set1))
set2={"a","e","i","o","u"}
print(any(set2))
# assigning to variable
set3={True and True,"fall",False or True,8,9-7j}
a=any(set3)
print(a)
#for empty set it will return False value
set4={}
b=any(set4)
print(b)
# using set as argument.
print(any({66,955.8,0,False,bool(0)}))
# condition for list any()
# True , True = True
# True , False / False , True = True
# False , False = False
# empty list = False 	 