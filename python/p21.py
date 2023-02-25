#else with loop

for i in range(5):
    print(i)
else:
    print("You are now out of range")

j=0
while j<7:
    print(j)
    j=j+1
    # if j == 4:
    #     break
else:
    print("You are out of range")

for x in range(5):
    print("iteration no {} in for loop".format(x+1))
else:
    print("else block in loop")
print("out of loop")