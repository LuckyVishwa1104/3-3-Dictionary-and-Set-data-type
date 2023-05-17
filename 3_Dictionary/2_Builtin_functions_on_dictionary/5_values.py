#5). valies() - this method return the list of values of dictionary 
#Syntax :   dict_name.values()
dict1={2:4,3:9,4:16,5:25,6:36}
print(dict1.values())
dict2={"a":"apple","b":"ball","c":"cat"}
print(dict2.values())
# assigning to a variable
dict3={"rup":"India","yen":"Japan","dol":"america"}
a=dict3.values()
print(a)
dict4={"[":"]","{":"}","(":")","<":">"}
b=dict4.values()
print(b)
# using with uninitialised dictionary
print({2:"int",3.4:"float","and":"str",True:"bool"}.values())