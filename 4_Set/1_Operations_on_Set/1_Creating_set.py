#4. Set - it is collection data-type, collection of unique(single existtance) items separated by ' , ' enclosed within curly braces '{ }' .
# elements of set are un-order, order is not fixed it is changing at every instance
# Set={val1, val2,val3, . . . , valn}
#1]. Creating or Declaring Set - 
''' Syntax :
	  set_name={val1, val2,val3, . . . , valn}
set_name = valid variable/identifier
value = all data-type( except List,Set,dict), variable, input, expression. '''

# set of numeric data-type integers.
set1={3,5,7,9,11,15}
print(set1)
set2={44,3.14,7-4j,0b110,0o64,0x2Ae}
print(set2)

# set of string and boolean data-type
set3={"sunday","minday","one",bool(0),True,False,bool("") }
print(set3) 

# set of tuple
set4={(2,4,6),(6,9),(6,9),(727),"$",67,8.3 }
print(set4)
print({(2),(77),47,"gg" })

# set of mixed data-type.
a,b,c=23,77,28
set5={a,b,c,a*b,a**c,77,"uu"}
print(set5)
set6={(a,b,a-c),34,2-a,"as",0b101,7.3,8-8j }
print(set6)