#6). all() - it return true value if all the keys are true.
# Syntax :    all(dict_name)
dict1={1:1.1,2:2.2,3:3.3,4:4.4,5:5.5}
print(all(dict1))
dict2={"a":"apple","b":"ball","v":"van",bool(0):False}
print(all(dict2))

# if dictionary is empty it return True
dict3={}
print(all(dict3))

# assigning to variables
a,b,c=2,4,9
dict3={False:a,bool(0.0):b,bool(False):c,False:15}
a=all(dict3)
print(a)

# passing dictionary as argument
print(all(dict({True:" ",False:None,bool(3):bool()})))

# conditions for dictionary all()
# True , True = True
# True , False / False , True = False
# False , False = False
# empty dictionary = True
