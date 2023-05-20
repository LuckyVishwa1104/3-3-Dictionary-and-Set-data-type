#2]. Set traversal - accessing elements of set one-by-one, it can be done by two ways.
# Traversal is applicable for particular instance only, since set are unordered index of elements changes for every iteration hence sequence of traversal also changes for every iteration.

#1). Using for loop - traverse all elements, usually done by for loop.
'''Syntax:  for elem. in set_name:
	                print(elem)  '''
print("1). Using for loop :")	 
# 1st example               
set1={2,4,6,8,10}
for ele in set1:
	print(ele)
# 2nd example
set2={"a","e","i","o","u"}
for val in set2:
	print(val)
# 3rd example
set3={"Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday" }
for var in set3:
	print(var)
# 4th example
for a in {True,False,bool(2),bool(""),None}:
	print(a)
print("Stop")

#2). Using enumerate() function - this function return the elements of set along with their index.
''' Syntax:  for val in enumerate(set_name):
	                    print(val)   '''
print("2). Using enumerate() function :")
# 1st example
set5={"Python","Java","C","C++","sql","JavaScript"}	
print(set5)
for ele in enumerate(set5):
	print(ele)
# 2nd example.
set6={2,4,6,8,10,0b100,0o56,0xAE}   
for b in enumerate(set6):
	print(b)
# 3rd example
for c in enumerate({"a","e","i","o","u","s","q"}):
	print(c)          
# 4th example
for d in enumerate({2,4,6,8,10,0b100}):
	print(d)
print("Finished")

# we can't use while for traversal as it is Not subsrcriptable