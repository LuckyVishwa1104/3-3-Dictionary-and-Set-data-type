#4]. Deleting element of set - removing elements of set, it is done by various methods.

#1). Using discard() method - it removes the specified elements.
#Syntax :  set_name.discard(element)
print("1). Using discard() metho :")
set3={"Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday" }
print(set3)
set3.discard("Monday")
set3.discard("Tuesday")
set3.discard("Wednesday")
set3.discard("Thursday")
# if element is not present set does'nt get changed.'
set3.discard("Noneday")
print("Holidays =",set3)

#2). Using remove() method - it also used to removes specified elements .
#Synyax:  set_name.remove(element)
print("2). Using remove() method :")
set2={"a","e","i","o","u","s","k","v","m" }
print(set2)
set2.remove("s")
set2.remove("m")
set2.remove("k")
set2.remove("v")
#if the element is not present in set, it will raise key error.
#set2.remove("a") - key error
print(set2)

#3). Using pop() method - it will remove and return the last element, since set are unordered any arbitarily no. will be erased.
#Syntax:  set_name.pop()
print("3). Using pop() method :")
set1={1,2,3,4,5,6,7,8,9,10}
print(set1)
set1.pop()
set1.pop()
set1.pop()
# assigning to variable
a=set1.pop()
b=set1.pop()
print(a,b)
print(set1)
