#6]. Dictionary Comprehension - it is an elegent way to create dictionary.
# writting code inside dictiomary and it will return in form of dictionary
#Syntax: {expression for item in iterable}
# expression must be in form of key:value pair.
print({item:item for item in range(1,6)})
print({ele:ele+1 for ele in range(2,10,2)})
dict1=({a:a*2 for a in [1,2,3,4,5]})
print(dict1)
dict2=({b:None for b in (2,4,6)})
print(dict2)
#1). using if 
dict3={a:"even"  for a in range(1,11) if a%2==0}
print(dict3)
dict4={"even":4,"odd":5,"even":6,"odd":7}
print({aa:bb for (aa,bb) in dict4.items() if bb >4 if bb%2==0})
#2). using if - else
dict5={k:("even" if k%2==0 else "odd") for k in range(1,11)}
print(dict5)
print({ag:("adult" if ag>18 else "child") for ag in [9,13,25,32,45]})
#3). using nested loop
dict8={ai:{ bi:ai for bi in range(1,5) } for ai in range(1,4)}
print(dict8)
print({j:{j:i+1 for i in range(1,3)} for j in range(1,5)})
