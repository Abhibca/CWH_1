#dictionary
dic ={
    "name" : "Abhi",
    "city" : "Rajkot",
    "state" : "Gujarat",
    "country" : "India"
}

print(dic)
print(type(dic))

print(dic["name"])
print(dic["city"])

print(dic.items())

print(dic.keys())
print(dic.values())

for key,value in dic.items():
    print(key,value)
    print(f"the value coresponding to the key {key} is {value}")