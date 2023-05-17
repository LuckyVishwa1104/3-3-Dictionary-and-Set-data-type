#2). fromkeys() - it cretes a dictionary from given sequence of keys and values.
# keys are only iterables(collection), same value is assigned to each keys.
''' Syntax :  
      dict.fromkeys(keys_seqn,values_seqn) 
keys = it can be only iterables (collections)  i.e. - list, tuple, set, dict, sequence, string
values = all data-types  '''
keys=(2,4,6)  
values="even_number"
print(dict.fromkeys(keys,values)) 
key1={1,3,5}
val1="odd_number"
print(dict.fromkeys(key1,val1))
# assigning to variables
key2=3,9,21
val2=3.01
a=dict.fromkeys(key2)
# if value is not assigned, it considers None value.
print(a)
key3="aeiou"
val3="vowels"
b=dict.fromkeys(key3,val3)
print(b)
# passing sequence as argument
print(dict.fromkeys((1,2,3),"integer"))