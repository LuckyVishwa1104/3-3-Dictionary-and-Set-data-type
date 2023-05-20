#6). items() - this methpd returns the list of elements of dictionary.
# Syntax :  dict_name.items()
dict1={2:4,3:9,4:16,5:25,6:36}
print(dict1.items())
dict2={"a":"apple","b":"ball","c":"cat"}
print(dict2.items())

# assigning to variables
dict3={"rup":"India","yen":"Japan","dol":"america"}
a=dict3.items()
print(a)
dict4={"[":"]","{":"}","(":")","<":">"}
b=dict4.items()
print(b)

# using uninitialized dictionary
print({2:"int",3.4:"float","and":"str",True:"bool"}.items())
