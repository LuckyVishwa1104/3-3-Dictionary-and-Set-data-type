#5]. Deleting elements of Dictionary - removing element of dictionary is done using different methods.

#1). Using .pop() method : it remove the key:value pair of specified key.
#Syntax: dict.pop("key",default)
print("1). Using pop() method :")
dict1=dict({1:"one",2:"two",3:"three",4:"four",5:"five"})
print(dict1)
# it return the vaule of deleted key
dict1.pop(1)
dict1.pop(3)
print("poped value is :",dict1.pop(4))
a=dict1.pop(5)
print("poped value is :",a)
# if key is not found it return the default value
print(dict1.pop(6,"key not found"))
print(dict1.pop(7,"key is missing"))
# if default value is not specified it raise key error
# print(dict1.pop(7))  // gives -> key error
print(dict1)

#2). Using .del() method : it delete the key:value pair of specified key.
#Syntax :   del dict_name[key]
print("2). Using del() method :")
dict2={2:"even",3:"odd",1:"unity",9:"mult. of 3",100:"ton"}
print(dict2)
del dict2[3]
del dict2[1]
# it does not return any value
del dict2[9]
del dict2[100]
del dict2[2]
# when key is not present it raises key error
#del dict2[10]  -> key error
print(dict2)

#3). Using popitem() method : it remove the last element of dictionay.
#Syntax :  dict_name.popitem()  
print("3). Using popitem() method :")
dict3=dict({1:0b001,2:0o35,3:0x3A,4:3.14,5:-78,6:-7+4j})
print(dict3)
dict3.popitem()
dict3.popitem()
dict3.popitem()
#it return the key:value pair of last element
b=dict3.popitem()
print("poped item is :",b)
print("poped item os :",dict3.popitem())
# it raises key error when dictionary is empty.
# display the dictionary
print(dict3)

