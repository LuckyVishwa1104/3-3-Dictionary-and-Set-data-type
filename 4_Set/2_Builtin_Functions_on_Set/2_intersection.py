#2). intersection() - this methid return the set, containing common elements  from both the sets.
# it can also be done using "&" operator
'''Syntax:set_name1.intersection(set_name2)
                  set_name1 & set_name2   '''            
set1={2,4,6,8,10}
set2={4,6,8,"o","u"}
set3={0b101,0o45,"o","u"}
print(set1.intersection(set2))
print(set2.intersection(set3))
print(set2 & set2)
# if on element are common it return empty set.
print(set1 & set3)
# assigning to variable
set4={10,"o","u",88,0.9 }
a=set2.intersection(set4)
print(a)
b=set4.intersection(set3.intersection(a))
print(b)
c=set2 & set4
print(c)
d=set4 & set3 & c
print(d)
# using set as argument
print({2,3,4}.intersection({3,4,5}))
print({2,3,4} & {3,4,5})