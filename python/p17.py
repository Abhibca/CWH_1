#Function recursion

def fectorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * fectorial(n-1)

print(fectorial(3))

def febonachi(n):
    if(n==0 or n==1):
        return 1
    else:
        return febonachi(n-1) + febonachi(n-2)
    
print(febonachi(6))