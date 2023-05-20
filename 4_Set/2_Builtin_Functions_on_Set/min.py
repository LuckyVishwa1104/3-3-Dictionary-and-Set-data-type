#5. min() - return the minimum element of set.
# for this function the set should contain elements of same data-type

#Syntax :   min(set_name) 
set1={2,4,6,8,10}
print(min(set1))
set2={2.2,4.5,6,7-8,10,0b101}
print(min(set2))

# assiging to variable
set3={1.1,1.11,1.111,1.1111}
a=min(set3)
print(a)

# for other than numeric data-type it consider ascii value for comparision.
set4={"a","e","i","o","u"} 
b=min(set4)
print(b)

# using as argument
print(min({"Python","Java","C","C++","sql","JavaScript"}))
