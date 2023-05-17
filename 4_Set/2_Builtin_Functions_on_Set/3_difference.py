#3). difference() - this method return the set of those element of first set which are not in second set.
# it can also be done using "-" operator.
'''Syntax: set_name1.difference(set_name2)
                set_name1 - set_name2   '''    
set1={2,4,6,8,10}
set2={4,6,8,"o","u"}
set3={0b101,0o45,"o","u"}
print(set1.difference(set2))          
print(set2.difference(set3))
print(set1 - set2)
print(set2 - set3)
# assigning to variable
set4={10,"o","u",88,0.9 }
a=set2.difference(set4) 
print(a)
b=set1.difference(set2.difference(set3))  
print(b)
c=set4 - set2
print(c)   
d=set3 - set2 - set1
print(d) 
# using set as argument
print({1,2}.difference({2,4}))  
print({""} -{""})
                                                       