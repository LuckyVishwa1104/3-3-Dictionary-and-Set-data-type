#5. Set Comprehension - creating new from existing set
# writing the code inside curly brackets

# Syntax:   {expression for item in range()}
set1={ele for ele in range(1,11)}
print(set1)
set2={ele+1 for ele in range(0,11,2)}
print(set2)

# using if 
set3={a for a in range(1,11) if a%2==0}
print(set3)
print({a1 for a1 in range(1,11) if a1%2!=0})

# using nested if 
set4={a2 for a2 in range(1,51) if a2%2==0 if a2%5==0}
print(set4)
print({a3 for a3 in range(0,11) if a3%2==0 if a3%2!=0})

# using if else 
set5={"even" if a4%2==0 else "odd" for a4 in range(1,11)}
print(set5)
age=int(input("Enter Your age : "))
print({"eligible for vaccination" if age>=18 else "not eligible for voting"})

# using nested loop
set6={i*j for i in range(1,6) for j in range(1,11)}
print(set6)

# first loop is the outermost loop
print({(x,y,z) for x in ("a","b","c") for y in ("x","y","z") for z in ("p","q","r")})
