#3. len() - return the length of set i.e. total.no of elements of set
#Syntax :  len(set_name)  
set1={2,4,6,8,10}
print(len(set1))
set2={"a","e","i","o","u"}
print(len(set2))
# assigning to variable
set3={"Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday" }
a=len(set3)
print("Days in week : ",a)
# it will not count the repeated elements
set4={2,4,6,8,10,2,5,2,6,7}
print(len(set4))
# using set as argument
print(len({"Python","Java","C","C++","sql","JavaScript"}))
