#2]. Accessing values of dictionary - by using key we can access the value of dict, there are two ways to access dictionary value.
dict={1:2,"o":"vowel","ceo":"54.8 cr ¥"}
print(dict[1])
print(dict["o"])
print(dict["ceo"])

#1). dict[key] - using key value we can access corresponding value.
#syntax:   dict_name[ 'key' ]
print("1). using [key] ")
dict1={"v":"violet","i":"indigo","b":"blue","g":"green","y":"yellow","o":"orange","r":"red"}
print(dict1["v"])
print(dict1["i"])
# assingning to variable
a,b=dict1["b"],dict1["g"]
print(a)
print(b,dict1["o"])
# it return key error when key is not in dict.  print(dict1["z"])
print(dict[1]*45,dict1["r"])

#2). get("key") - able to access value at particular key, it is nore prefered over above method because it handels the key not found error.
#Syntax:   dict_name.get("key","prompt")
print("2). Using get(key):")
v,n=5.5,-8
dict2={0b101:"int 5",7-4j:"complex",(2,4,9):"squares",v:"variable",v+n:["expression"]}
print(dict2.get(0b101))
print(dict2.get(7-4j))
# assigning to variable
j,k=dict2.get((2,4,9)),dict2.get(v)
print(j)
print(k,dict1.get("o"))
# it return "None" value when key is not present
print(dict2.get("no"))
print(dict1.get(76),dict2.get(v))
# when prompt is used and value is not present then prompt is displayed.
print(dict2.get("key","key is not present"))
print(dict2.get("value","value named key is not present"))
