#6). intersection_update() - this method perform intersection of two set and assign result to first set and then update the result of intersection to first set.
#Syntax: set1.intersection_update(set2)
set1={2,4,6,8,10}
set2={4,6,8,"o","u"}
set3={0b101,0o45,"o","u"}
set1.intersection_update(set2)
print(set1)
set2.intersection_update(set3)
print(set2)
# it does not return any value(None)
a=set1.intersection_update(set2)
print(a)
print(set1)
set4={10,"o","u",88,0.9 }
set4.intersection_update(set2)
print(set4)
set2.intersection_update(set2,set1)
print(set2)