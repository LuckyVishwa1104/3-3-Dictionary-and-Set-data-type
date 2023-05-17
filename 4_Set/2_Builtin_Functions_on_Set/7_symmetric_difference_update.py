#7). symmetric_difference_update() - this method perform symmetric difference of two set and assign result to first set and then update the result of symmetric difference to first set.
''' Syntax:
	set1.symmetric_difference_update(set2) '''
set1={2,4,6,8,10}
set2={4,6,8,"o","u"}
set3={0b101,0o45,"o","u"}
set1.symmetric_difference_update(set2)
print(set1)
set2.symmetric_difference_update(set3)
print(set2)
# it does not return any value(None)
a=set3.symmetric_difference_update(set2)
print(a)
print(set3)
set4={10,"o","u",88,0.9 }
set4.symmetric_difference_update(set2)
print(set4)
set1.symmetric_difference_update(set4)
print(set1)