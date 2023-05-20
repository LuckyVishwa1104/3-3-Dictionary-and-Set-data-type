#9). update([]) - it add new value to specified key or adds new key:value to dictionary.
'''Syntax: dict_name.update([(key,value),...])
parameter = iterables(list, tuple, set, string(2 alphabates)) '''
dict1={2:4,3:9,4:16,5:25,6:36}
print(dict1)
dict1.update([(9,81)])
dict1.update([(10,100)])

# if key is present, then it update its value
dict1.update([[2,22],"no",(33,44)])
dict1.update([{11,121},(888,49)])
print(dict1)

# it return None value 
dict2={"a":"apple","b":"ball","c":"cat"}
print(dict2.update([("y","n")]))

# Primarily this method is used to add new dictionary to pre-existing dictionary.
dict3={"inr":"India","yen":"Japan","dol":"America"}
dict4={"riyal":"Soudi","daman":"UAE"}
dict3.update(dict4)
print(dict3)

# using dictionary as argument
dict4.update({"[":"]","{":"}","(":")","<":">"})
print(dict4)
