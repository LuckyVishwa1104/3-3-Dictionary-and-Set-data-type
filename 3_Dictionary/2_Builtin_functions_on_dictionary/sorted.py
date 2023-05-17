#5). sorted() - it sort i.e. arrange the keys of dictionary in increasing order and return the list of keys.
# key must be of same data-type for comparision.
#Syntax :   sorted(dict_name)
dict1={1:1.1,2:2.2,3:3.3,4:4.4,5:5.5}
print(sorted(dict1))
# for other than numeric data-type it consider asscii value for comparision.
dict2={"a":"apple","b":"ball","v":"van"}
print(sorted(dict2))
# assigning to variable
a,b,c=2,4,9
dict3={1:a,2:b,3:c,4:15}
print(sorted(dict3))
dict4={"[":"]","{":"}","(":")","<":">","•":"°"}
a=sorted(dict4)
print(a)
# passing dictionary as argument
print(sorted({1.01:11,2.2:22,3.03:33}))