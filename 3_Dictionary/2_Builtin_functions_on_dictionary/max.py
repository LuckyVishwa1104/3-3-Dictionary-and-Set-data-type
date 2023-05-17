#2). max() - it return the maximum ie. largest key among all the keys.
# for this, the keys should be of compairable data-type.
# Syntax:  max(dict_name)
dict1={1:1.1,2:2.2,3:3.3,4:4.4,5:5.5}
print(max(dict1))
# for other than numeric data-type it consider asscii value for comparision.
dict2={"a":"apple","b":"ball","v":"van"}
print(max(dict2))
# assigning to variables
a,b,c=2,4,9
dict3={1:a,2:b,3:c,4:15}
print(max(dict3))
dict4={"[":"]","{":"}","(":")","<":">","•":"°"}
a=max(dict4)
print(a)
# using dictionary as argument
print(max({1.01:11,2.2:22,3.03:33}))
