#3). Updating Set elements - changing or modifying elements of set, since set are unordered elements can't be updated using index.
# There are two methods to update set element.

#1). Using add() method - it adds single element to set at any index.
# Syntax:   set_name.add(element)
print("1). Using add() method :")
set1={2,4,6,8,10}
print(set1)
set1.add(12)
set1.add(14)
set1.add(None)
set1.add("sad_lyfe")
print(set1)
# it returns None value.
print({22,33,44}.add(55))

#2). Using update() method - it adds sequence of element to set in random order.
# Syntax:  set_name.update(sequence)
print("2). Using update() method :")
set2={"a","e","i","o","u"}
print(set2)
set2.update("uh","jj") 
set2.update(["x","y","z"])
set2.update("lucky")
set2.update([777,888,"hola"],{"queen",True},(23,77))
print(set2)
# it return None value.
print({None}.update({2:4,3:9,4:16}))
