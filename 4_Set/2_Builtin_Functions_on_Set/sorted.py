#9. sorted() - it arrange the element of list in increasing order.
# elements should be of comparable data-type.
#Syntax:  sorted(set_name)
set1={2,4,6,8,10}
print(sorted(set1))
set2={2.2,4-7,6,0b101,8,10}
print(sorted(set2))
# assigning to variables
set3={0b10,0o45,0xAE,98}
a=sorted(set3)
print(a)
# for other than numeric value it compares ascii value.
set4={"a","e","i","o","u","z"}
a=sorted(set2)
print(a)
# using set as argument
print(sorted({1.1,1.01,1.001,1.0001}))