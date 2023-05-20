#7). pop() - this method remove the key:value pair of specified key. It return the value of specified key.
# Syntax:   dict_name.pop(key,default)
dict1={2:4,3:9,4:16,5:25,6:36}
print(dict1)
dict1.pop(2)
dict1.pop(3)
print(dict1.pop(4))
print(dict1)

# assigning to variable.
dict2={"a":"apple","b":"ball","c":"cat"}
a=dict2.pop("a")
print(a)
b=dict2.pop("b")

# if key is not found then it return the default value.
print(dict2.pop("d","key not found"))

# if default value is not assigned it raises key error.
# print(dict2.pop("d"))  >> key error
