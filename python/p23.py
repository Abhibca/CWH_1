#Finally

def func1():
    try:
        l = [1,5,9,2,4]
        i = int(input("Enter the index : "))
        print(l[i])
        return 1
    except:
        print("Some error occured ")
        return 0
    
    finally:
        print("finally is always executed")

x = func1()
print(x)