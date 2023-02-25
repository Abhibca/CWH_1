#function argument

def default(a=10, b=20):
    return a * b  

c= default()
print(c)

def require(fname, lname="Sindhav"):
    print("Hello ",fname,lname)

require("Abhishek")
require("Abhishek","Rajput")