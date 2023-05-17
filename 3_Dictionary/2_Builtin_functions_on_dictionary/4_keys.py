#4). keys() - it return the list of keys of dictionaries
#Syntax :  dict_name.keys()
dict1={2:4,3:9,4:16,5:25,6:36}
print(dict1.keys())
dict2={"a":"apple","b":"ball","c":"cat"}
print(dict2.keys())
# assigning to variables
dict3={"rup":"India","yen":"Japan","dol":"america"}
a=dict3.keys()
print(a)
dict4={"[":"]","{":"}","(":")","<":">"}
b=dict4.keys()
print(b)
# using with uninitialised dictionary
print(dict({2:"int",3.4:"float","and":"str",True:"bool"}).keys())
