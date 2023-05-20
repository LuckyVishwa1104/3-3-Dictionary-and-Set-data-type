#3). get() - it return the value of specified key
#Syntax : dict_name.get(key,default)

dict2={"a":"apple","b":"ball","c":"cat"}
print(dict2.get("a"))
print(dict2.get("b"))

# assigning to variable
a=dict2.get("c")
print(a)

# if key is not present then it return None
b=dict2.get("d")
print(b)

# if key is not present and default value is assigned then it return default value.
print(dict2.get("f","not found"))
print({"L":"Lucky","V":"Vishwakarma"}.get("L"))
