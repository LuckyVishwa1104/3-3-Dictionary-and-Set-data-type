#4]. Updating element of dictionary - dictionary are partially mutable we can only update values but not keys of dict.
# values of the dictionary are mutable but keys are immutable and unique.

#1). dict[key] - using this method we can change value of that respective key or can add new key:value pair.
# Syntax :'''  dict_name[key]=value '''
print("> Using dict[key] method")
dict1={2:"two",3:"three",4:"four",5:"five"}
print(dict1)

dict1[2]="two_2"
dict1[3]="three_3"
dict1[4]="four_4"
dict1[1]="one_1"
a=6
dict1[a]="six_6"
print(dict1)

#2). update() - using this method we can add new key:value pair and can add another dictionary.
# Syntax: dict_name.update(key:value)
print("> Using .update([]) method")
dict_2={"harry":"present","peter":"on shoot","ryuga":"the strongest"}
dict_3={"light":"better world"}
print(dict_2)

dict_2.update([("rock","inarena"),("lucky","moving toward his goals")])
dict_2.update([("harry","potter")])
dict_2.update([("saitama","saturday sale")])
dict_2.update([("peter","parker")])
dict_3.update([("peter","poker")])
dict_2.update(dict_3)
print(dict_3)
print(dict_2)
