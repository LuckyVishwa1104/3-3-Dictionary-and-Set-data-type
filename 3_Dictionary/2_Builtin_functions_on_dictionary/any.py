#7). any() - it return true value when any of the dictionary key is true.
# Syntax -  any(dict_name)
dict1={1:1.1,2:2.2,3:3.3,4:4.4,5:5.5}
print(any(dict1))
dict2={False:77,bool(0):True,True:None}
print(any(dict2))
# it return false value for empty dictionary.
empty={None:None}
print(any(empty))
# assigning to variable
a,b,c=2,4,9
dict3={False:a,bool(0.0):b,bool(False):c,False:15}
d=any(dict3)
print(d)
# using dictionary as parameter
print(any(dict({True:" ",False:None,bool(3):bool()})))
# condition for dictionary any()
# True , True = True
# True , False / False , True = True
# False , False = False
# empty dictionary = False
