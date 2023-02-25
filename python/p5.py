#Strings

A = "Hello My name is Abhishek!!!"

print(len(A))
print(A)
print(A.upper())
print(A.lower())
print(A.rstrip("!"))
print(A.replace("Abhishek","Sindhav"))
print(A.split(" "))
print(A.capitalize())
print(A.center(50))
print(len(A.center(50)))
print(A.count("Abhi"))
print(A.endswith("!"))
print(A.find("is"))
print(A.index("is"))

str1 = "WelcomeToTheConsole"
print(str1.isalnum())

str1 = "Welcome"
print(str1.isalpha())

str1 = "welcome"
print(str1.islower())

str1 = "Welcome\n"
print(str1)
print(str1.isprintable())

str1 = "Welcome to the programming world"
print(str1.istitle())

str1 = "Welcome"
print(str1.startswith("Welcome"))

str1 = "Welcome to the programming world"
print(str1.swapcase())

str1 = "Welcome to the programming world"
print(str1.title())

