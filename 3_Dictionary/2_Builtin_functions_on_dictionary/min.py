#3). min() - it return the min i.e least key of available keys of dictionaries.
# keys should be of compairable data-type
#Syntax :   min(dict_name)
dict1={1:1.1,-2:2.2,3:3.3,4:4.4,5:5.5}
print(min(dict1))
# for other than numeric data-type it consider asscii value for comparision.
dict2={"a":"apple","b":"ball","v":"van"}
print(min(dict2))
# assigning to variables
a,b,c=2,4,9
dict3={1:a,2:b,3:c,4:15,8:44,0.0:0.00}
print(min(dict3))
dict4={"[":"]","{":"}","(":")","<":">","•":"°"}
a=min(dict4)
print(a)
# passing dictionary as argument
print(min({1.01:11,2.2:22,3.03:33}))
