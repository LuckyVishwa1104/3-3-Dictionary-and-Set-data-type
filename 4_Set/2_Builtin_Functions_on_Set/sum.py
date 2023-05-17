#6. sum() - return the sum of all elem. of set
# For sum function the set should contain element of same data-type.
# Synatx:   sum(set_name,value) 
# valid only for numeric and bool data-type
set1={2,4,6,8,10}
print(sum(set1))
set2={2.2,3.3,4.5}
print(sum(set2))
# assigning to variable
set_non={0b110,0o134,0x12A,87,9.00} 
a=sum(set_non)
print(a)
# it also accept second parameter "value", it is added to sum of set elem.
set_com={2+7j,-8-5j,89,0.3,0b10}
b=sum(set_com,10)
print(b)
# using set as argument
print(sum({8,9.3,True,False}))
