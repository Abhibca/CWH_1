#while Loop

i = 0
while(i<=10):
    print(i)
    i = i + 1
else:
    print("the loop is over")


j = 0
for j in range(12):
    if(j==10):
        break
    print("5 X ",j+1,"=",5*(j+1))
    
print("Leave the Loop")
    
j = 0
for j in range(12):
    if(j==10):
        print("Leave the iteration")
        continue
    print("5 X ",j+1,"=",5*(j+1))
    
