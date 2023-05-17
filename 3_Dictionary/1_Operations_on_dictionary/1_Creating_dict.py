#3. Dictionary data-type - dictionary is a collection of elem. in "key:value" pair separeted by commas and enclosed within curly braces .
# dicitonary are partially mutable datatype only the value part is mutable and key is unique.
# Dictionary={key1:val1, key2:val2, key3:val3, - - -, keyn:valn}

#1]. Creating or declaring dictionary.
''' Syntax: 
dictionary_name={key1:val1, key2:val2, key3:val3, - - -, keyn:valn}
dictionary_name= (a to z, A to Z, 0 to 9, _)
key = all data-type( except List, Set, Dict), variable, input, expression .
value = all data-type, variable, expression, input .'''

#1. dictionary of numeric data
dict_num={1:0b001,2:0o35,3:0x3A,4:3.14,5:-78,6:-7+4j}  
print(dict_num)
dict_num2={1:1,2:4,3:9,4:16,5:25}     
print(dict_num2)

#2. dict of string and bool
dict1={1:"one",2:"two",3:"three",4:"four",5:"five"}
print(dict1)
print({"True":bool(3),"false":bool(0),True:0b1110})

#3. dict of mixed data
dict_mix={(2,3):"Azeri","money can buy anything":"yes",67:["&","@"],"key":"value"}
print(dict_mix)
dict_mix2={"¶":"charecter",():(),7-3j:{8:7,6:3},None:2*5*6}
print(dict_mix2)

#4. dict of complex data
a,b,c,d="wwe",5,7,3.4
dict_com={a:"quit",7-8:b,c*d:d*c,(a,b):[c,d,b+d],0b101:b**2}
print(dict_com)
dict_com2={input("key 1 :"):input("value 1 :"),input("key 2 : "):input("value 2 : ")}
print(dict_com2)
