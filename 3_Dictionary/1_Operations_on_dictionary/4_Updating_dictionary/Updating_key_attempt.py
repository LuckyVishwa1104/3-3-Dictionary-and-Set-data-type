# Changing keys of dictionary :
''' Since keys are unique and immutable they can't be modified, but indirectly using different merhods it can be modified. '''

#1). Using del() function : Assiging key value to new key and deleting previous key
print("Using del() function :")
# create a dictionary
dict={1:"one",2:"two",3:"three",4:"four"} 
print("Before Updating :",dict)
# suppose 2nd element key is to be updated 
# assign that key value to a variable to store that value
a=dict[2]
# delete the 2nd element key
del dict[2]
# assign new key to that value
dict[22]=a
# display the dictiinaryl
print("After updating :",dict)

#2). Using pop() method : Assingn key value to variable and delete key using pop() function 
print("Using pop() method :")
# create a dictionary 
dict1={"a":"apple","b":"ball","c":"cow","d":"dog"}
print("Before updating",dict1)
# suppose "c" key is to be modified.
# assign value of "c" to a variable.
b=dict1.get("c")
# delete the "c" key using pop() method
dict1.pop("c")
# assign new key to "cow" value
dict1["e"]=b
# display the dictionary
print("After updation :",dict1)

# there are 3 more methods by which keys can be modified.
# for more info visit : (https://www.delftstack.com/howto/python/change-the-key-in-a-dictionary-in-python/)
