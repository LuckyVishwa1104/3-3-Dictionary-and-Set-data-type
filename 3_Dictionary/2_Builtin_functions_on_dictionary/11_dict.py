#11). dict() - dict constructor creates dictionary of given parameters.
# there are three ways dictionary can be constructed using dict()

#a). using mapping - it accept dictionary of key:value sequence and return it.
dict3=dict({2:4,3:9,5:25}) 
dict4=dict({1.1:11,2.2:22,3.3:33})
print(dict3)
print(dict4)
print(dict({1:"one1",2:"two",3:"three"}))

#b). using keyargs - i.e. key arguments , variable along with their value are considered as key:value pair.
# Syntax:   dict(var1=val1,var2=val2,....,                                     varn=valn)
# keys should be undeclared variables only
dict1=dict(x=2, y=4, z=6)
print(dict1)
dict2=dict(p="even",q="odd", r="even")
print(dict2)
print(dict(u=4, v=16, w=36))

#c). using iterables - passing dict the collection of key,value pairs in iterable form.
# Syntax: dict([(key1,val1),[key2,val2],....,{keyn,valn}])
dict5=dict([(3,88),[8,7],{8,3}])
dict6=dict(((3.2,67),[87,33],"st"))
print(dict5) 
print(dict6)
print(dict({(55,66),(77,90),"er"}))