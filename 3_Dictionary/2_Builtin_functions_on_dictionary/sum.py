#4). sum() -  it return the sum of all the keys of dictionary.
# dictionary must contain element of compairable data-type, its applicable to numeric and bool data_tyle 
# Syntax:  sum(dict_name) 
dict1={1:1.1,2:2.2,3:3.3,4:4.4,5:5.5}
print(sum(dict1))
dict2={1:"a",2:"b",3:"c",4:15}
print(sum(dict2))
# assigning to variable
a,b,c=0b101,0o45,0x1AE
dict3={a:12,b:24,c:36,4:15}
d=sum(dict3)
print(d)
# passing dictionary as argument
print(sum({2:20,3-7j:44,0b101:False,True:None}))
# for empty dictionary sum is zero.
print(sum({}))
