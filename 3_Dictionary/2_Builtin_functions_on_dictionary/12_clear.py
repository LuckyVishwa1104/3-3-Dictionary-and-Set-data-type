#8). clear() - it clear or empty the entire dictionary.
#Syntax :   dict_name.clear()
dict1={1:1.1,2:2.2,3:3.3,4:4.4,5:5.5}
dict1.clear()
print(dict1)
dict2={"a":"apple","b":"ball","v":"van"}
dict2.clear()
print(dict2)

# it does not return any value (None value)
a,b,c=2,4,9
dict3={1:a,2:b,3:c,4:15}
a=dict3.clear()
print(a)

# it does not accept any parameter
dict4={"[":"]","{":"}","(":")","<":">","•":"°"}
print(dict4.clear())
print(dict4)

# using dictionary as argument
print({1.01:11,2.2:22,3.03:33}.clear())
