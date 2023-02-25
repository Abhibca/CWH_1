#list

l = [1,2,3,4,"Abhi",678,"Sindhav",78,90]

print(l) 
print(l[0])
print(l[5])
print(l[7])

print(l[:])
print(l[0:len(l):2])

if "Ab" in l[4]:
    print("Yes")
else:
    print("No")

lst = [i*i for i in range(11)]
print(lst)

lst = [i*i for i in range(11) if i%2==0]
print(lst)