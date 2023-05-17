# There is more elegent way to iterate through dictionary.

#3). keys() - used to iterate the keys of dict.
# it return a list of keys.
''' Syntax:
	   for var in dict.keys():
	   	print(var)  '''
dict1={"A":"a","B":"b","C":"c","D":"d","E":"e"}
dict2={1:0b001,2:0b010,3:0b011,4:0b100}
print(dict1.keys())
print(dict2.keys())
# using for loop
for a in dict1.keys():
	print(a)
for b in dict2.keys():
	print(b)
for s in {1:11,2:22,3:33}.keys():
	print(s)
	
#4). values() - used to iterate values of dict.  it return the list of values.
'''Syntax:
	   for var in dict.values():
	   	print(var)  '''
dict3={5:"int",6-7j:"complex","ff":"string",8.3:"float"}
print(dict3.values())
print(dict1.values())
# using for loop
for c in dict3.values():
	print(c)
for d in dict1.values():
	print(d)
for l in {1:1.1,2:2.2,3:3.3,4:4.4}.values():
	print(l)
	
#5). items() - this is the most elegent ways to iterate dict. (it is actual iteration of dictionary)
# it iterate both keys and values, it return the list of tuples of key:value pair.
''' Syntax:
	   for var in dict.items():
	   	print(var)  '''
dict4={1:"one",2:"two",3:"three",4:"four"}
print(dict4.items())
print(dict2.items())
# using for loop
for e in dict4.items():
	print(e)
for f in dict2.items():
	print(f)
for g in dict3.items():
	print(g)
