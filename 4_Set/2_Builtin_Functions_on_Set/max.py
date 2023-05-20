#4. max() - return the maximum element of set.
# for this function the set should contain element of compairable data-type

#  Syntax :   max(set_name)
set1={2,4,6,8,10}
print(max(set1))
set2={2.2,4.5,6,7-8,10,0b101}
print(max(set2))

# assiging to variable
set3={1.1,1.11,1.111,1.1111}
a=max(set3)
print(a)

# for other than numeric data-type it consider ascii value for comparision.
set4={"a","e","i","o","u"} 
b=max(set4)
print(b)

# using as argument
print(max({"Python","Java","C","C++","sql","JavaScript"}))