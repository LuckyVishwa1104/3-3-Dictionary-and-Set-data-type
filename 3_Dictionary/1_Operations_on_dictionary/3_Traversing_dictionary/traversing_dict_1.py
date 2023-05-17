#3]. Traversing a dictionary - printing all element of dict. one by one.
# As other collection data-type uses index and loop for traversal, while using these method for dictionary it produce different result, hence dictionary uses different method to traverse(dictionary failure).

#1). Using for loop.
'''Syntax: 
  for var in dict_name:
	  print(var,dict_name[var])  '''
print("Using for loop.")	  
dict1={5:"int",6-7j:"complex","ff":"string",8.3:"float"}
dict2={"name":"Lucky","class":"SE-B","branch":"computer","roll no.":2263,}	 
dict3={10:"83.4%",11:"62%",12:"79.94%","FE":"9.5sgpa"}
# it will only iterate keys of dict.
for i in dict1:
	 print(i)
for j in dict2:
	print(j)	
# using dict_name[key]/.get(key) function
# example 1
for var in dict2:
	print(var,dict2[var])
for k in dict3:
	print(k,":",dict3.get(k))
# example 2
for l in dict1:
	print(l,dict1[l])
for m in dict2:
	print(m,":",dict2.get(m))
	
#2). Using enumerate function - display index and corresponding elem.
'''Syntax:
	  for var in enumerate(dict_name):
	  	print(var,dict[key]/.get(key))  '''
print("Using enumerate function.")	  	
dict4={"windos":11,"macOS":15,"linux":None}
dict5={"K":1000,"M":"1000k","B":"1000M"}
# it will only display index and keys of dict.
for n in enumerate(dict4):
	print(n)
for o in enumerate(dict5):
	print(o)
# we can't use dict_name[key]/.get(key) function while iterating with enumerate.
for p in enumerate(dict1):
	print(p)
