#10). setdefault() - it return the value of specified key.
# Syntax :  dict_name.setdefault(key,value)
dict1={2:4,3:9,4:16,5:25,6:36}
print(dict1)
print(dict1.setdefault(2))
print(dict1.setdefault(3))

# If key is not present then it add specified key:value pair.
dict1.setdefault(7,49)
dict1.setdefault(8,64)
print(dict1)

# assigning to variable
a=dict1.setdefault(7)
b=dict1.setdefault(8) 
print(a,b)

# it return None value if key not found and default is not assigned
print(dict1.setdefault(9))

# using with unintialized dictionary
print({"a":"apple","b":"ball","c":"cat"}.setdefault("a"))
