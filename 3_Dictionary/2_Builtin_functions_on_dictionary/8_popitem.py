#8). popitem() - it remove and return the last element of dictionary.
# Syntax :  dict_name.popitem()
dict1={2:4,3:9,4:16,5:25,6:36}
print(dict1)
dict1.popitem()
dict1.popitem()
print(dict1)
dict2={"a":"apple","b":"ball","c":"cat"}
print(dict2)
print(dict2.popitem())
# assigning ti variable
a=dict2.popitem()
b=dict2.popitem()
print(dict2)
# using dictionary as parameter.
print({"[":"]","{":"}","(":")"}.popitem())