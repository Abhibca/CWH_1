#Tupple

tup = (1,2,3,4,"Abhi",678,"Sindhav",78,90)

print(tup) 
print(tup[0])
print(tup[5])
print(tup[7])
print(tup[:])
print(tup[0:len(tup):2])

if "Ab" in tup[4]:
    print("Yes")
else:
    print("No")

tp = (i for i in range(11))
print(tp)

tp = (i*i for i in range(11) if i%2==0)
print(tp)