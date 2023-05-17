# Various built-in functions and methods :    there are different methods or function that can be performed on dictionaries. 
#1). len() : return the total no. of element of dictionary.
# Syntax:    len(dict_name)
dict1={1:1.1,2:2.2,3:3.3,4:4.4,5:5.5}
print(len(dict1))
dict2={"a":"apple","b":"ball","v":"van"}
print(len(dict2))
# using variables 
a,b,c=2,4,9
dict3={1:a,2:b,3:c,4:15}
print(len(dict3))
dict4={"[":"]","{":"}","(":")","<":">","•":"°"}
a=len(dict4)
print(a)
# using dictionary as argument
print(len({1:11,2:22,3:33}))