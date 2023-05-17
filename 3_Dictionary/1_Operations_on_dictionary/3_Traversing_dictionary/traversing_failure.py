#3]. Traversing failure.
#1). Using for loop - it only traverse keys.
dict={2:4,3:9,4:16,5:25,6:36}
for val in dict:
	print(val)
print("stop")
#2). Using range function with loop - it also traverse keys, if index is not present as key it throws key error.
dict1={1:1,2:8,3:27,4:64,5:125}
for i in range(1,len(dict1)):
	print(dict1[i])
print("stop")
#3). Using enumerate function - it will also traverse keys only and return them along with their index.
dict2={"one":1,"two":2,"three":3,"four":4,"five":5}
for en in enumerate(dict2):
	print(en)
print("stop")