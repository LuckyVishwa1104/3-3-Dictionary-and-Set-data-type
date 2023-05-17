# There are some ofnimportant methods build purely tonimplement dictionary. 
#1). copy() - it create and return shallow copy of dictionary. 
# Syntax:  dict_name.copy()
dict1={2:4,3:9,4:16,5:25,6:36}
print(dict1.copy())
dict2={"a":"apple","b":"ball","c":"cat"}
print(dict2.copy())
# assigning to variable
dict3={"rup":"India","yen":"Japan","dol":"america"}
a=dict3.copy()
print(a)
dict4={"[":"]","{":"}","(":")","<":">"}
dict5=dict4.copy()
print(dict5)
# passing dictionary as argument
print({2:"int",3.4:"float","and":"str",True:"bool"}.copy())